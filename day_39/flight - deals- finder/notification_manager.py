import smtplib
import os


class NotificationManager:
    def __init__(self, info:list):
        self.list_data = info

    def mail_sender(self):

        with smtplib.SMTP("smtp.gmail.com", 587) as conection:     # start the mail sending
            password = os.environ.get("GMAIL_Pass")     # api for gmail
            user = "danielfaruzz@gmail.com"        # sender mail
            conection.starttls()
            conection.login(user=user, password=password)
            for data in self.list_data:
                msg = "Subject: deal ALART \n\n" + data  #massega from data frame
                conection.sendmail(from_addr=user, to_addrs="danielfaruz@gmail.com", msg=msg)


