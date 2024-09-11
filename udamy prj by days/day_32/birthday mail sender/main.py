import pandas
import smtplib
from random import randint
import datetime as dt
import os
# i need tto import the csv data as a dataframe to the  code:
data = pandas.read_csv("birthdays.csv")

# taping into datetime module to get the current day month and year

today = dt.datetime.now()
t_year = today.year
t_month = today.month
t_day = today.day

# we need to check the i some index in the list have birthday today :

# Check if any row in the DataFrame has a birthday today
birthday_today = data[(data["month"] == t_month) & (data["day"] == t_day)]

if not birthday_today.empty:  # statement to check if the data is empty or not birthday_today is dataframe with filters
    print("Some one have birthday today yaiii")
    for (index, value) in birthday_today.iterrows():

        print(f"congrats {value['name']} is {t_year - int(value['year'])} years old mail sent")  #check data sent

        with open(f"letters/letter_{randint(1,3)}.txt") as letter_data: # creating a random text letter

            letter = letter_data.read()      # import the data
            letter = letter.replace("[NAME]", value['name'])      #  replace the [NAME] with the data name

        with smtplib.SMTP("smtp.gmail.com") as conection:     # start the mail sending

            msg = f"congrats {value['name']} is {t_year - int(value['year'])} years old"  #massega from data frame
            password = os.environ.get("GMAIL_Pass")     # api for gmail
            user = "danielfaruzz@gmail.com"        # sender mail
            conection.starttls()
            conection.login(user=user, password=password)
            conection.sendmail(from_addr=user, to_addrs=value["email"], msg=f"Subject: {msg} \n\n"+letter)
else:
    print("no birthday today")
