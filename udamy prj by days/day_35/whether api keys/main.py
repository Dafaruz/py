import os
import requests
from twilio.rest import Client

# ____________________________ part for the client sms user  api + token + number ______________

p_number = '+16123516006'   # number we send from
Account_SID = os.environ.get("Twilio_API_SID")
Auth_Token = os.environ.get("Twilio_API_KEY")
# ____________________________ part for the whether site api + token ______________
api_key = os.environ.get("Weather_API_KEY")
whether_site = "https://api.openweathermap.org/data/2.5/forecast"


lat = 31.862339
lon = 35.165318
param = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "unit": "metric",
    "cnt": 4
}

client = Client(Account_SID, Auth_Token)       # create  object  with the api ket and id

whether_request = requests.get(url=whether_site, params=param)   # get the whether with the param dict
print(whether_request.status_code)     # checking the HTML code if 200 we are good
whether_request.raise_for_status()

data = whether_request.json()       # convert to json

for index in range(0, len(data["list"])):    # go throw the list

    if data["list"][index]["weather"][0]["id"] < 700:    # 700 its id top rain in the api so if id <700 its rainy

        message = client.messages.create(       # crate message object to send via  twilio
            from_='whatsapp:+14155238886',
            body=f'in day: {index + 1} take an umbrella',
            to='whatsapp:+972548318600'

        )
        print(message.status) # print the status of the message

