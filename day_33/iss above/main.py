import smtplib
from datetime import datetime
import requests
MY_LAT = 31.863400
MY_LON = 35.171890

my_parameter = {"lat": MY_LAT, "lon": MY_LON, "formatted": 0}

s_s_request = requests.get(url="https://api.sunrise-sunset.org/json?lat=36.7201600&lng", params=my_parameter)
s_s_request.raise_for_status()
s_s_data = s_s_request.json()
home_sunset_t = float(s_s_data["results"]["sunset"].split("T")[1].split(":")[0])
home_sunrise = float(s_s_data["results"]["sunrise"].split("T")[1].split(":")[0])


iss_pos_request = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_pos_request.raise_for_status()

iss_pos_data = iss_pos_request.json()
iss_lat = float(iss_pos_data["iss_position"]["latitude"])
iss_lon = float(iss_pos_data["iss_position"]["longitude"])


today_time = datetime.now()
time_h = float(today_time.hour)

if time_h == 0.0:  # 24 hour cycle
    time_h = 24


mail_msg = (f" Subject: ISS is above you \n\n the location of iss lat: "
            f"{iss_lat}, lon : {iss_lon}, your home is {MY_LON, MY_LON}")
if home_sunrise < time_h > home_sunset_t:
    if MY_LAT-5 >= iss_lat <= MY_LAT+5 and MY_LON-5 >= iss_lon <= MY_LON+5:

        with smtplib.SMTP("smtp.gmail.com") as conection:
            password = "zmgi pdtz czfw hdnl"
            user = "danielfaruzz@gmail.com"
            conection.starttls()
            conection.login(user=user, password=password)
            conection.sendmail(from_addr=user, to_addrs="danielfaruz@gmail.com", msg=mail_msg)
    else:
        pass


