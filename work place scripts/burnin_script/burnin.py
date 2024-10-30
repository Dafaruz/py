##################################################################################
#                                                                                #
# Author: Lalawe, Hsen                                                           #
# Name:   burnin_test.py                                                         #
# Description: Execute burnin_test app, Validate Passed in Logs                  #
#                                                                                #
##################################################################################
#                                                                               ##
#               INTEL CORPORATION PROPRIETARY INFORMATION                       ##
#   This software is supplied under the terms of a license agreement or         ##
#   nondisclosure agreement with Intel Corporation and may not be copied        ##
#   or disclosed except in accordance with the terms of that agreement.         ##
#                                                                               ##
#       Copyright (c) 2022 Intel Corporation. All Rights Reserved.              ##
#                                                                               ##
##################################################################################
##################################################################################
#  Import Modules                                                                #
##################################################################################
import argparse
import subprocess
from datetime import datetime
import shutil
import sys
import os
import time
import re


##################################################################################
#  Init Global Test Handler                                                      #
##################################################################################
def assign_globals():
    sys.path.append(r"C:\validation\windows-test-content\gfx\common")
    from test_handler import TestHandler

    global global_th
    global_th = TestHandler("BURNIN", False, "gfx")


##################################################################################
#  Func:  to parse user args                                                     #
##################################################################################
def parse_args():
    try:
        parser = argparse.ArgumentParser(description='Parsing all arguments')
        ######################################################
        #  Scop: Args Expect Value                           #
        ######################################################
        parser.add_argument('--bitcfg_path', '-cfg ', default="", help='Burnin cfg Path - required')
        parser.add_argument("--time", "-t", default="60", help='time in mins')
        parser.add_argument("--extra_time_out", "-extout", default="2", help='time out after time is finish, In Mins')
        parser.add_argument("--log_src", "-ls",
                            default="C:\\Users\\Administrator\\Documents\\PassMark\\BurnInTest\\BIT_log.log",
                            help='Default log path by Burnin settings')
        ######################################################
        #  Scop: Args Stores True/ False - Actions           #
        ######################################################
        parser.add_argument("--debug_logs", "-dbg", action='store_true', help='For debug logs')

        args = parser.parse_args()
    except:
        global_th.error_exit("failed_to_parse_args", 4)
    global_th.log.info(f"Finish parse_args: {args}")
    return args


##################################################################################
#  Globals                                                                       #
##################################################################################
def timestamp():
    return datetime.now().strftime('#%d_%m_%Y#%H_%M_%S_%f')


##################################################################################
#  Class: BurninTest, Execute Burnin with specific CFG, Handle Process           #
##################################################################################
class BurninTest:
    def __init__(self, args, th=None) -> None:

        ######################################################
        #  Scop: Validate TestHandler Creation               #
        ######################################################
        if th is None:
            assign_globals()
            th = global_th
        self.th = th

        ######################################################
        #  Scop: Attributes From Args                        #
        ######################################################
        self.bit_cfg_path = args.bitcfg_path
        # self.time = args.time
        self.time = self.th.optimize_to_mins(args.time)
        self.extra_time_out_in_sec = eval(args.extra_time_out) * 60
        self.debug_logs: bool = args.debug_logs

        ######################################################
        #  Scop: Attributes Of Object                        #
        ######################################################
        self.bit_path = '"' + os.environ["Burnin"] + '"'
        self.default_log_path = args.log_src
        self.log_file_name_dist = "bit_log" + timestamp() + ".log"
        self.dist_log_path = os.path.join(os.getcwd(), self.log_file_name_dist)

        ######################################################
        #  Scop: Attributes with Generation                  #
        ######################################################
        self.command = None
        self.is_time_out = False
        self.errors_list = []
        self.th.log.info("Finish Init BurninTest Object: " + str(self.__dict__))

    ##################################################################################
    #  Func: execute_actions                                                         #
    ##################################################################################
    def execute_actions(self):

        self.th.print_empty_line()
        self.th.log.info('Start execute_actions')

        ######################################################
        #  Scop: Delete Old Logs If Exists                 #
        ######################################################
        self.delete_logs_if_exists()
        ######################################################
        #  Scop: Create & Execute Command                    #
        ######################################################
        self.command = self.generate_command()
        self.exe_command()

        if self.is_time_out:
            self.th.log.warning(
                f'command time out, it may cause from config file not configured well, Trying to reach the logs')
        ######################################################
        #  Scop: Sleep To Validate Logs Created              #
        ######################################################
        sleep_time = 25
        self.th.log.info(f'Sleeping {sleep_time} seconds, for ensure Burnin finish running')
        time.sleep(sleep_time)
        ######################################################
        #  Scop: Move Logs To CWD, Search For Passed String  #
        ######################################################
        self.move_log_to_dist()
        self.get_errors_summary()
        self.is_passed_in_log()

        self.th.log.info('Finish execute_actions')
        self.th.print_empty_line()

    ##################################################################################
    #  Func: generate_command                                                        #
    ##################################################################################
    def generate_command(self):
        command = f"{self.bit_path}"

        if self.debug_logs:
            command += f" -u"

        command += ' -R' \
                   + ' -D ' + str(self.time) \
                   + ' -C \"' + self.bit_cfg_path + '\"'
        self.th.log.info(f'Finish generate_command, command returned: {command}')
        return command

    ##################################################################################
    #  Func: exe_command                                                             #
    ##################################################################################
    def exe_command(self):
        self.th.log.info('Start exe_command: ' + str(self.command))

        self.th.rep_data_command_list.append(f"{self.command}")
        # time_in_secs = eval(self.time) * 60 + self.extra_time_out_in_sec
        time_in_secs = self.time * 60 + self.extra_time_out_in_sec
        try:
            self.th.log_test_handler.info(f"{self.command}")
            bit_process = subprocess.run(self.command, timeout=time_in_secs, check=True)
            self.th.log.info(f"bit_process.stdout : {bit_process.stdout}")
        except subprocess.TimeoutExpired:
            # the command took longer than the timeout period
            self.th.log.warning(f"Command timed out, timeout is {time_in_secs} sec")
            self.is_time_out = True
            return

        except subprocess.CalledProcessError as e:
            # the command returned a non-zero exit status
            self.th.log.warning(f"Command timed out : {e.stdout}")
            self.th.error_exit(f"running_burnin_failed.after_start.with_error_return_code[{bit_process.returncode}]", 3)

        if bit_process.returncode != 0:
            self.th.error_exit(f"running_burnin_failed.after_start.with_error_return_code[{bit_process.returncode}]", 3)

    ##################################################################################
    #  Func: move_log_to_dist                                                        #
    ##################################################################################
    def move_log_to_dist(self):
        if os.path.exists(self.default_log_path):
            self.th.log.info("default_log_path Exists : " + self.default_log_path)
        else:
            self.th.error_exit(f"the_attribute.default_log_path.is_not_existing[{self.default_log_path}]", 1)

        shutil.copyfile(self.default_log_path, self.dist_log_path)

        if os.path.exists(self.dist_log_path):
            self.th.log.info("Logs Copied to:" + str(self.dist_log_path))
        else:
            self.th.error_exit(f"filed_to_copyfile_to_dist_log_path[{self.dist_log_path}]", 1)

    ##################################################################################
    #  Func: is_passed_in_log                                                        #
    ##################################################################################
    def is_passed_in_log(self):
        # passed_str = '\x00T\x00E\x00S\x00T\x00 \x00R\x00U\x00N\x00 \x00P\x00A\x00S\x00S\x00E\x00D\x00\n'
        passed_str = "TEST RUN PASSED"
        with open(self.dist_log_path, "r") as src_file:
            for line in src_file:
                line_x = line.replace("\x00", "")
                line_x = line_x.replace("\n", "")
                if passed_str in line_x:
                    self.th.log.success(f"Found, The String: {passed_str}")
                    self.th.log.info(f"In The Line: {line_x}")
                    self.th.log.info(f"In Log File: {self.dist_log_path}")
                    return True
            self.th.print_proc_list()
            self.th.print_event_log_list(mins_ago=f'{int(self.time)}')
            self.th.error_exit(f"passed_string_is_not_found_in_burnin_logs[Search for passed_str: {passed_str}]", 1)

    ##################################################################################
    #  Func: get_errors_summary                                                        #
    ##################################################################################
    def get_errors_summary(self):

        try:
            summary_str = 'SERIOUS ERROR SUMMARY FOR THE LAST TEST RUN'
            finish_summary = '------------------'
            ignore_in_summary = '**************'
            store_lines = False
            with open(self.dist_log_path, "r") as src_file:
                for line in src_file:
                    line_x = line.replace("\x00", "")
                    line_x = line_x.replace("\n", "")
                    if finish_summary in line_x:
                        break
                    if summary_str in line_x:
                        store_lines = True
                        continue
                        # Check if we should store this line
                    if store_lines and (line_x != "") and (ignore_in_summary not in line_x):
                        self.errors_list.append(line_x.strip())

            if len(self.errors_list) == 0:
                self.th.log.info("error list length is 0, suspect no errors in burnin logs")
                return
            for line in self.errors_list:
                test_str = f"{line.split(',')[1].strip()}"
                err_kind_str = f"{line.split(',')[2].split(':')[0].strip()}"
                err_suffix_str = f"{line.split(',')[2].split(':')[1].strip()}"
                msg = f"{test_str}.{err_kind_str}.{err_suffix_str}".strip()
                msg = re.sub(r'\s+', '_', msg)
                msg = msg.replace(' ', '')
                msg = msg.replace('(', '[').replace(')', ']')
                self.th.handle_error(f"{msg}", 1)
        except Exception as err:
            self.th.log.warning(f"Got Exception while tring to get the errors from self.dist_log_path {err}")

    ##################################################################################
    #  Func: delete_logs_if_exists                                                   #
    ##################################################################################
    def delete_logs_if_exists(self):
        if os.path.exists(self.default_log_path):
            self.th.log.info("default_log_path Exists, deleting")
            os.remove(self.default_log_path)
        else:
            self.th.log.info("default_log_path is empty")


################################################################################################
#  Main_flow Start -> parse_args -> BurninTest Obj creation -> execute_actions                 #
################################################################################################
def main_flow():
    try:
        assign_globals()
        global_th.log.info('Start main_flow')

        bit_obj = BurninTest(parse_args(), global_th)
        bit_obj.execute_actions()

        ######################################################
        #  Scop: Pass Criteria, Errors                       #
        ######################################################
        if global_th.error_cnt == 0:
            global_th.pass_exit()

    except Exception as err:
        global_th.handle_error(err, 2)
    finally:
        global_th.finalize_test()


if __name__ == "__main__":
    main_flow()

##################################################################################
#  Commands Ex. to run in CMD                                                    #
##################################################################################

# python C:\validation\windows-test-content\gfx\common\applications\burnin_test.py -t 480 -cfg C:\validation\windows-test-content\gfx\common\burnin_scenes\low3dStress.bitcfg
# python C:\validation\windows-test-content\gfx\common\applications\burnin_test.py -t 2 -cfg C:\validation\windows-test-content\gfx\common\burnin_scenes\low3dStress.bitcfg
# python C:\validation\windows-test-content\gfx\common\applications\burnin_test.py -t 2 -cfg C:\validation\windows-test-content\gfx\common\burnin_scenes\low3dStress.bitcfg --debug_logs
# python C:\validation\windows-test-content\gfx\common\applications\burnin_test.py -t 2 -cfg C:\validation\windows-test-content\gfx\common\burnin_scenes\low3dStress.bitcfg -ls "C:\\Users\\Administrator\\Documents\\PassMark\\BurnInTest\\BIT_log"

##################################################################################
#  Comments                                                                      #
##################################################################################
"""
# How to prepare bitcfg 
#     Configuration -> Test Selection& Duty Cycles -> On Last Used Set the expected Configs 
#         Select settings Gear
#             go to Pre/Post Test -> in PASSED & FAILED set Action to Run External application & exit*
#             go to Logging -> Turn automatic logging on 
#                 Log file name -> "C:\\Users\\Administrator\\Documents\\PassMark\\BurnInTest\\BIT_log"
#                 Log name prefix -> Single file
#                 ok -> ok 
#     File -> Save Test Configuration As -> choose name without spaces 
# 
# If you are know where Burnin Log File located (Via bitcfg you Prepared) use Like: -ls "C:\\Program Files (x86)\\BurnInTest\\BIT_log.log" 
"""
