from random import randint

print(randint(0,3))










        with smtplib.SMTP("smtp.gmail.com") as conection:

            msg = f"congrats {value['name']} is {t_year - int(value['year'])} years old"  #massega from data frame
            password = "zmgi pdtz czfw hdnl"     # api for gmail
            user = "danielfaruzz@gmail.com"        # sender
            conection.starttls()
            conection.login(user=user, password=password)
            conection.sendmail(from_addr=user, to_addrs="danielfaruz@gmail.com", msg="Subject: Daily Quote \n\n"+msg)
