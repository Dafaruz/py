import smtplib
import datetime as dt
from random import choice


work_week = dt.datetime.now()    # get the date and time of now
work_week = work_week.weekday() # set the work week value
print(work_week)
if work_week == 3:
    with open("quotes.txt", mode="r", encoding="utf-8") as txt:
        quotes_list = txt.readlines()

    with smtplib.SMTP("smtp.gmail.com") as conection:
        msg = f"Subject: Daily Quote \n\n {choice(quotes_list)}"
        print(msg)
        password = "zmgi pdtz czfw hdnl"
        user = "danielfaruzz@gmail.com"
        conection.starttls()
        conection.login(user=user, password=password)
        conection.sendmail(from_addr=user, to_addrs="danielfaruz@gmail.com", msg="Subject: Daily Quote \n\n"+msg)





