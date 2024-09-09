import smtplib
import os


class NotificationManager:
    def __init__(self, info:list):
        self.list_data = info

    def mail_sender(self):
        with smtplib.SMTP("smtp.gmail.com") as conection:     # start the mail sending
            for data in self.list_data:
                msg = data  #massega from data frame
                password = os.environ.get("GMAIL_Pass")     # api for gmail
                user = "danielfaruzz@gmail.com"        # sender mail
                conection.starttls()
                conection.login(user=user, password=password)
                conection.sendmail(from_addr=user, to_addrs="danielfaruz@gmail.com", msg=msg)


