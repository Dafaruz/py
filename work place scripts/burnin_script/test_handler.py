##################################################################################
#                                                                                #
# Author: Lalawe, Hsen                                                           #
# Name:   test_handler.py                                                        #
# Description:  Handle Script With Result Standardization, Reporter & Logging,   #
#               Error Codes, Fail/Pass Criteria, Fails Count                     #
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
import os
import sys
import time
import inspect
import argparse
import traceback
from datetime import datetime
import svtools.logging.toolbox
from logging import Formatter
import psutil
from prettytable import PrettyTable

sys.path.append(r"C:\validation\windows-test-content\gfx\common\media_utils")
from event_logs import EventLog

try:
    try:
        sys.path.append(r"c:\validation\auto-pack\standalone\reporter")
        import insight_reporter as reporter
    except:
        sys.path.append(r"c:\svshare\pce_enabling\standalone\reporter")
        import reporter
    from svtools.report import Report
except Exception as e:
    print(e)

##################################################################################
#  Globals                                                                       #
##################################################################################
def timestamp():
    return datetime.now().strftime('#%d_%m_%Y#%H_%M_%S_%f')[:-3]


##################################################################################
#  Class: TestHandler, Logger, Errors, Insight, Execution Info                   #
##################################################################################
class TestHandler:
    def __init__(self, tool_name="TEST_HANDLER", fixed_log_name=False, ip_domain="missed_domain") -> None:

        ######################################################
        #  Scop: Base Attributes                             #
        ######################################################
        self.tool_name = tool_name
        self.ip_domain = ip_domain
        self.log_name = tool_name + "_logger"

        ######################################################
        #  Scop: Fixed Log File/ with Timestamp              #
        ######################################################
        self.log_time_stamp_ext = timestamp()
        if fixed_log_name:
            self.log_file_name = tool_name + ".log"
        else:
            self.log_file_name = tool_name + self.log_time_stamp_ext + ".log"

        ######################################################
        #  Scop: Attributes with Generation                  #
        ######################################################
        self.formatter = Formatter("%(asctime)s [%(levelname)s] %(module)s(%(lineno)d) : %(message)s")
        self.log = self.init_logging()
        self.log_test_handler = self.init_test_handler_log()
        self.report_name = None
        self.rep = None
        self.rep_data_command_list = []
        self.messages_list = []

        ######################################################
        #  Scop: Test Result Start at fail status, err count #
        ######################################################
        self.start_time = time.time()
        self.finish_time = None
        self.test_res = 1
        self.error_cnt = 0
        self.parent_cmd = ""

        self.add_introduction_to_log()
        self.add_command_to_log()
        self.print_empty_line()
        self.log.info(f"Finish Init TestHandler Object: {self.__dict__}")
        self.log.info("Finish Preparations *********************************************************************************************")
        self.print_empty_line()

    ##################################################################################
    #  Func: init_logging, Default Attributes                                        #
    ##################################################################################
    def init_logging(self):
        # TODO: Optimize and Rebuild the initials of the logging
        log = svtools.logging.toolbox.getLogger(self.log_name, autosplit=True)
        log.setFile(self.log_file_name)
        log.setConsoleFormat("time")
        # log.setFileFormat(Formatter("%(asctime)s: %(levelname)s: %(module)s(%(lineno)d) : %(message)s"))
        log.setFileFormat(self.formatter)
        log.colorLevels(True)
        return log

    ##################################################################################
    #  Func: init_test_handler_log, Default Attributes                               #
    ##################################################################################
    def init_test_handler_log(self):
        log_test_handler = svtools.logging.toolbox.getLogger("test_handler_commands", autosplit=True)
        log_test_handler.setFile(f'test_handler_commands.log')
        log_test_handler.setFileFormat(Formatter("%(asctime)s: %(message)s"))
        return log_test_handler

    ##################################################################################
    #  Func: init_report                                                             #
    ##################################################################################
    def init_report(self):
        # TODO: Optimize initials of the Report
        self.report_name = self.tool_name + timestamp()
        rep = Report(self.report_name)
        self.log.info(f"Init Report Object, report_name: {self.report_name}")
        return rep

    ##################################################################################
    #  Func: update_rep_summary, updates Report Summary                              #
    ##################################################################################
    def update_rep_summary(self, summary, update_exit=False):
        self.rep.summary = summary
        if update_exit:
            sys.exit(1)

    ##################################################################################
    #  Func: update_report_data, Commands                                            #
    ##################################################################################
    def update_report_data(self):
        for command in self.rep_data_command_list:
            self.rep.std.content.add_data(self.tool_name, version="1", commandline=command)
            self.log.info(f"Report, update_report_data: {self.tool_name}, version=\"1\", commandline={command}")

    ##################################################################################
    # Func: handle_error, Supports Report Insight, Errors Handle, codes, TraceBack   #
    # err_code=1 -> (Default) unexpected result, insight                             #
    # err_code=2 -> (Python) Exception -> uncovered_exception                        #
    # err_code=3 -> Execute command , cmd                                            #
    # err_code=4 -> System Issues/ Input not valid                                   #
    # err_code=99 -> Global Checker                                                  #
    ##################################################################################
    def handle_error(self, err, err_code=1):
        self.print_empty_line()
        self.log.info("*********************************************************************************************")
        self.log.error(f"err_code={err_code} , err: {err}")

        ######################################################
        #  Scop: err is TypeError / err is msg               #
        ######################################################
        if isinstance(err, TypeError) or isinstance(err, ValueError) or isinstance(err, NameError) or \
                isinstance(err, KeyError) or isinstance(err, IndexError) or isinstance(err, IOError) or err_code == 2:
            self.log.info(traceback.format_exc())
        else:
            self.log.info("Traceback Start ***************************************************************************")
            self.log.info(traceback.format_exc())
            self.log.info("Traceback Finish **************************************************************************")

            frame, filename, line_number, function_name, lines, index = inspect.stack()[2]
            head, tail = os.path.split(filename)
            #self.log.error(f"{tail}({line_number}), Func: {function_name}, LineContent: [{lines[0].strip()}], Index: {index}")

            table_fail_point = PrettyTable()
            table_fail_point.field_names = ["Title", "Detail"]
            table_fail_point.align = "l"
            table_fail_point.add_row(["Script Name", f"{tail}"])
            table_fail_point.add_row(["Fail Func", f"{function_name}"])
            table_fail_point.add_row(["Fail Line", f"{line_number}"])
            table_fail_point.add_row(["Line Content", f"{lines[0].strip()}"])
            table_fail_point.add_row(["Index", f"{index}"])
            self.log.info("\n============================")
            self.log.info("  Fail Point Details")
            self.log.info("============================")
            self.log.info(f"{table_fail_point}")

        ######################################################
        #  Scop: Generate reporter if is not yet             #
        ######################################################
        if self.rep is None:
            self.rep = self.init_report()
        else:
            self.log.info(f"Report Object Already Created, report_name: {self.report_name}")

        ######################################################
        #  Scop: uncovered_exception                         #
        ######################################################
        if err_code == 2:
            err = "uncovered_exception"

        ######################################################
        #  Scop: create_insight                              #
        ######################################################
        if err_code == 1 or err_code == 2 or err_code == 3 or err_code == 4 or err_code == 99:
            err = err.upper()
            try:
                self.messages_list.append([time.strftime("%H:%M:%S", time.localtime()), f"{err}"])
                self.rep.std.content.create_insight(self.tool_name, ip_domain=self.ip_domain, result="FAIL",
                                                    error_code=err_code, message=str(err))
                self.log.info(
                    f"Report, create_insight: {self.tool_name}, ip_domain={self.ip_domain}, result=\"FAIL\", error_code={err_code}, message={err}")

            except Exception as e:
                self.log.error(f"create_insight Error={e}")
                error_msg = f"create_insight_with_all_details_failed.during_{self.tool_name}_error.{err}"
                self.rep.std.content.create_insight("TEST_HANDLER", result="FAIL", error_code=err_code,
                                                    message=error_msg.upper())

        self.test_res = 1
        self.error_cnt += 1
        self.log.info(f'Finish handle_error, test_res={self.test_res}, error_cnt={self.error_cnt}')
        return self.test_res

    ##################################################################################
    #  Func: finalize_test, Finishing Execution, Handle Finishing                    #
    ##################################################################################
    def finalize_test(self):
        self.print_empty_line()

        self.log.info("Start finalize_test *********************************************************************************************")

        if self.error_cnt > 1 and self.rep.summary is not None:
            self.update_rep_summary(f"test_handler.execution_failed_with_errors[errors_cnt: {self.error_cnt}]", update_exit=False)
            self.log.info(f'Report Summary: {self.rep.summary}')

        ######################################################
        #  Scop: Update report_data                          #
        ######################################################
        if self.rep is not None:
            self.log.info(f"Report Object Is Created, Error/s Occurs")

            self.update_report_data()
            reporter.save(self.rep)
            if self.rep.summary is not None:
                self.log.info(f"Report Summary: {self.rep.summary}")
        else:
            self.log.info(f"Report Object Is Not Created, No Error/s Occurs")

        ######################################################
        #  Scop: Summary                                     #
        ######################################################
        self.log.info(f'Commands Count \"Prepared For Report\": {len(self.rep_data_command_list)}')
        self.finish_time = time.time()
        self.print_messages_table()

        table = PrettyTable()
        table.field_names = ["Title", "Status"]
        table.align = "l"

        self.print_clean_log("\n+============================+")
        self.print_clean_log("  Script Run Status Summary")
        self.print_clean_log("+============================+")

        #self.log.info(f"Runtime: {(self.finish_time - self.start_time) / 60.0:.2f} minutes")
        table.add_row(["Runtime (Mins)", f"{(self.finish_time - self.start_time) / 60.0:.2f}"])
        #self.log.info(f'Errors Count: {self.error_cnt}')
        table.add_row(["Errors Count", f"{self.error_cnt}"])
        #self.log.info(f'Return Code Result: {self.test_res}')
        table.add_row(["Test Result", f"{self.test_res}"])

        # Return Exit Code
        return_code = self.test_res
        if self.test_res == 1:
            if os.getenv('GEC', None):
                return_code = 99
                self.log.info(f"Env Var GEC detected, Expected global checker test with return code {return_code}")
            else:
                self.log.info(f"Env Var GEC did not detected, No Global checker expected")

            table.add_row(["Return Code", f"{return_code}"])
            table.add_row(["END Final Status ", f"Failed"])
            self.print_clean_log(f"{table}")
            self.log.error('Failed')
            self.log.closeFile()
            sys.exit(return_code)
        else:
            table.add_row(["Return Code", f"{return_code}"])
            table.add_row(["END Final Status ", f"Passed"])
            self.print_clean_log(f"{table}")
            self.log.success('Passed')
            # self.log.info("=== END ===")
            self.log.closeFile()
            sys.exit(0)

    ##################################################################################
    #  Func: error_exit, Update Errors, Finishing                                    #
    ##################################################################################
    def error_exit(self, err, err_code=1):
        self.handle_error(err, err_code)
        # For global checker handling
        if os.getenv('GEC', None) and err_code == 99:
            self.log.info(f"Env Var GEC detected, Expected global checker test with return code 99")
            sys.exit(99)
        sys.exit(1)

    ##################################################################################
    #  Func: pass_exit, Finishing                                                    #
    ##################################################################################
    def pass_exit(self):
        self.test_res = 0
        sys.exit(0)

    ##################################################################################
    #  Func: print_proc_list                                                         #
    ##################################################################################
    def print_proc_list(self):
        self.log.info(f"CPU, Cores Count:  {psutil.cpu_count()}")
        self.log.info(f"CPU Usage, Percent:  {psutil.cpu_percent(interval=1, percpu=False)}")
        self.log.info(f"CPU Usage, Percent By CPU:  {psutil.cpu_percent(interval=1, percpu=True)}")
        self.print_clean_log("\n============================")
        self.print_clean_log("  Process List For Track")
        self.print_clean_log("============================")
        table = PrettyTable()
        table.field_names = ["PID", "Name", "CPU (%)", "Memory (MB)", "Username"]
        processes = list(psutil.process_iter())

        for process in processes:
            try:
                process_details = process.as_dict(attrs=['pid', 'name', 'memory_info', 'username'])
                pid = process_details['pid']
                name = process_details['name']
                username = process_details['username']
                memory_mb = round(process_details['memory_info'].rss / (1024 * 1024), 2)
                cpu_usage = process.cpu_percent(interval=0.2)
                table.add_row([pid, name, cpu_usage, memory_mb, username])
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as exp:
                self.log.warning(f"print_proc_list Func Raised psutil Exception as: {exp}")
                pass

        sorted_table = table.get_string(sortby="CPU (%)", reversesort=True, sort_key=lambda row: (row[3], row[4]))
        # self.log.setFileFormat(Formatter("%(message)s"))
        # self.log.info(f"{sorted_table}")
        # self.log.setFileFormat(self.formatter)
        self.print_clean_log(f"{sorted_table}")

    ##################################################################################
    #  Func: print_event_log_list                                                    #
    ##################################################################################
    def print_event_log_list(self, mins_ago=15, sleep_sec=60):
        self.log.info(f"sleeping {sleep_sec} Seconds, then try to get windows event log in last {mins_ago} Minutes Ago")
        time.sleep(sleep_sec)
        ev_obj = EventLog(argparse.Namespace(minsAgo=mins_ago), self)
        ev_obj.execute_actions()

    ##################################################################################
    #  Func: print_event_log_list                                                    #
    ##################################################################################
    def print_empty_line(self):
        # self.log.setFileFormat(Formatter("%(message)s"))
        # self.log.info(f"")
        # self.log.setFileFormat(self.formatter)
        self.print_clean_log(f"")

    ##################################################################################
    #  Func: print_clean_log                                                         #
    ##################################################################################
    def print_clean_log(self, out_put):
        self.log.setFileFormat(Formatter("%(message)s"))
        self.log.info(f"{out_put}")
        self.log.setFileFormat(self.formatter)

    ##################################################################################
    #  Func: add_command_to_log                                                      #
    ##################################################################################
    def add_command_to_log(self):
        self.parent_cmd = "python"
        for argument in sys.argv:
            self.parent_cmd += " " + argument

        self.print_one_row_table(["Global repro Command", f"{self.parent_cmd}"])
        self.print_one_row_table(["Script usage help   ", f"python {sys.argv[0]} --help"])
        self.log_test_handler.info(f"{self.parent_cmd}")
        # self.log.info(f"Command: {command}")

    ##################################################################################
    #  Func: print_one_row_table                                                     #
    ##################################################################################
    def print_one_row_table(self, row):
        table = PrettyTable()
        table.add_row(row)
        table.header = False
        table.align = "l"
        self.print_clean_log(f"{table}")

    ##################################################################################
    #  Func: print_messages_table                                                     #
    ##################################################################################
    def print_messages_table(self):
        table = PrettyTable()
        table.field_names = ["Time", "Message"]
        table.align = "l"

        for row in self.messages_list:
            table.add_row(row)
        self.print_clean_log("\n============================")
        self.print_clean_log("  Messages List For Insight")
        self.print_clean_log("============================")
        self.print_clean_log(f"{table}")

    ##################################################################################
    #  Func: add_introduction_to_log                                                 #
    ##################################################################################
    def add_introduction_to_log(self):

        intro_str = "      ___           ___           ___                       ___\n     /\__\         /\  \         /\  \        " \
            "  ___        /\  \ \n    /::|  |       /::\  \       /::\  \        /\  \      /::\  \ \n   /:|:|  |     " \
            " /:/\:\  \     /:/\:\  \       \:\  \    /:/\:\  \ \n  /:/|:|__|__   /::\~\:\  \   /:/  \:\__\      " \
            "/::\__\  /::\~\:\  \ \n /:/ |::::\__\ /:/\:\ \:\__\ /:/__/ \:|__|  __/:/\/__/ /:/\:\ \:\__\ \n " \
            "\/__/~~/:/  / \:\~\:\ \/__/ \:\  \ /:/  / /\/:/  /    \/__\:\/:/  / \n       /:/  /   \:\ \:\__\    \:\  " \
            "/:/  /  \::/__/          \::/  / \n      /:/  /     \:\ \/__/     \:\/:/  /    \:\__\          /:/  / \n " \
            "    /:/  /       \:\__\        \::/__/      \/__/         /:/  / \n     \/__/         \/__/         \/__/" \
            "                     \/__/ "

        formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.start_time))
        welcome_msg = "Test Handler Started\n\n" \
                      "  Do Not Forget To\n" \
                      "   Check WARNINGS\n\n\n" \
                      "     Start Time\n" \
                      f"{formatted_time}\n\n" \
                      "     Good Luck"
        self.print_one_row_table([f"{welcome_msg}", f"{intro_str}"])
        # self.print_one_row_table(["Test Handler Started"])
        # self.print_clean_log(f"{intro_str}")

    ##################################################################################
    #  Func: optimize_to_mins                                                        #
    ##################################################################################
    def optimize_to_mins(self, input_value):
        """
        Converts input values in various time formats to minutes.
        Args:
            input_value (str or int): Input time in digits, string, or formatted string (e.g., '720:sec', '12:min', '0.2:hour').

        Returns:
            float: Time in minutes.
        """
        # If input is a digit or a digit in string format, directly convert to float
        if isinstance(input_value, int) or (isinstance(input_value, str) and input_value.isdigit()):
            return float(input_value)

        # Process formatted input
        if isinstance(input_value, str):
            # Convert input to lower case to handle case insensitivity
            input_value = input_value.lower()

            # Check for specific time formats and convert
            if ':sec' in input_value:
                # Extract the number before ':sec' and convert seconds to minutes
                seconds = float(input_value.split(':sec')[0])
                return seconds / 60.0
            elif ':min' in input_value:
                # Extract the number before ':min'
                return float(input_value.split(':min')[0])
            elif ':hour' in input_value:
                # Extract the number before ':hour' and convert hours to minutes
                hours = float(input_value.split(':hour')[0])
                return hours * 60.0
            elif '.' in input_value:
                return float(input_value)

        # In case of unexpected format, return None or raise an error
        return None


