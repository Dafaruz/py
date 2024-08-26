import os
import requests
from twilio.rest import Client
from datetime import datetime as dt, timedelta
import json

p_number = '+16123516006'   # number we send from
Account_SID = os.environ.get("Twilio_API_SID")
Auth_Token = os.environ.get("Twilio_API_KEY")


client = Client(Account_SID, Auth_Token)


def stock_news():

    for feed in news_data["feed"]:
        title = (f" according to the {feed['title']}  :\n\n {feed['summary']}  "
                 f"source : {feed['source_domain']} ")
        for ticker in feed["ticker_sentiment"]:
            if ticker["ticker"] == "TSLA":
                stats = (f" overall score is : {ticker['ticker_sentiment_score']}  "
                         f"and ticker label: {ticker['ticker_sentiment_label']}")
            return title + stats

# Your API key is: 5542115c1dd449069bde57cc9b51d454

today = dt.now().date()

# Get yesterday date by subtract x day (timedelta(days=x)) from today

yesterday = today - timedelta(days=2)     # a nive way to go x or more day to the back


key_4_all_api = os.environ.get("Alphavantage_API_KEY")  # get api from the env on os

param_stock_data ={
    "apikey": key_4_all_api,
    "function": "TIME_SERIES_INTRADAY",
    "symbol": "TSLA",
    "interval": "30min"
}

param_news_data ={
     "apikey": key_4_all_api,
     "function": "TIME_SERIES_INTRADAY",
     "symbol": "TSLA",
     "interval": "30min"
}
#_______________________________________ get data from site ________________________________________________

# stock_stat_request = requests.get(url="https://www.alphavantage.co/query",params=param_stock_data)
# stock_stat_request.raise_for_status()
# stock_data = stock_stat_request.json()


# news_request = requests.get(url="https://www.alphavantage.co/query", params=param_news_data)
# news_request.raise_for_status()
# news_data = news_request.json()

#_____________________________________________________________________________________________________________#

start_price = None
end_price = None

##################################################################################################################
with open("data.json", mode="r") as data:
    stock_data = json.load(data)

with open("New's.json", mode="r") as News:
    news_data = json.load(News)

##################################################################################################################
for (index, val) in dict.items(stock_data):

    if ("16:00:00" in index or "09:30:00" in index) and str(yesterday) in index:

        if "09:30:00" in index:
            morning_stats = f"in day: {index} the opening day the sell was : {val['1. open']} "
            start_price = float(val['1. open'])
        else:
            end_day_stats = f"in day: {index} the end of the day the sell was : {val['4. close']} "
            end_price = float(val['4. close'])

if end_price is not None and start_price is not None:       # need to check it's not empty
    change_via_day = end_price - start_price

    stock_status = f" change in stock today was: {round(change_via_day,5)}$ |" \
                   f"|  in %--> {change_via_day*100//start_price}%"

    user_message = stock_status + (stock_news())

message = client.messages.create(       # crate message object to send via  twilio
    from_='whatsapp:+14155238886',
    body=user_message,
    to='whatsapp:+972548318600'

)
print(message.status)  # print the status of the message
