import requests
import os
from datetime import datetime, timedelta
from data_manager import DataManager

proxy = {

    'http': 'http://proxy-chain.intel.com:911',
    'https': 'http://proxy-chain.intel.com:912',
}


# class to search for data in the api


class FlightSearch:

    def __init__(self):
        self.api_key = os.environ.get("AMADEUS_API_KEI")
        self.api_secret = os.environ.get("AMADEUS_API_SECRET")
        print(self.api_secret, self.api_key)
        self.token = self.get_new_token()
        self.price_end_point = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        self.price_data = {
            "originLocationCode": "TLV",
            "destinationLocationCode": "DATA_IN",
            "departureDate": (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d"),  # get the date for next weekend
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "USD",
            "max": 3
        }
        self.header = {"Authorization": f"Bearer {self.token}",
                       "accept": "application/vnd.amadeus+json"}

    def get_new_token(self):  # this function get token from api

        header = {"content-type": "application/x-www-form-urlencoded"}

        body = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }

        data = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token", headers=header,
                             data=body).json()

        print(f"your generate token is :  {data['access_token']}\n")
        print(f"pls notice this token will end in {data['expires_in']} sec")

        return data['access_token']  # self.token get the token from the server

    def search_price(self, data_manager: DataManager):

        data_list = []
        data_of_prices = data_manager.data  # will get list of dictionaries to work with
        for data in data_of_prices['prices']:
            self.price_data["destinationLocationCode"] = data["iataCode"]
            price_data = requests.get(url=self.price_end_point, headers=self.header,
                                      params=self.price_data, ).json()

            i = 0
            local = 0

            try:
                for index in range(0, int(price_data["meta"]["count"])-1): # finde the bast value price index
                    if i > float(price_data['data'][index]['price']['grandTotal']):
                        i = float(price_data['data'][index]['price']['grandTotal' ])
                        local = index

                try:
                    city = data['city']
                    price = price_data['data'][local]['price']['grandTotal']
                    tickets = price_data['data'][local]['numberOfBookableSeats']

                    print(f" flight to {city} is {price} $ ")

                    if float(price_data['data'][local]['price']['grandTotal']) < float(data['lowestPrice']):
                        data = f"the flight to {city} is SALE at: {price}$ pls notice there is {tickets} tickets free"
                        data_list.append(data)
                    else:
                        print(f'no deals today for flights to : {city}' )

                except (KeyError, IndexError):

                    print(f"no flights to: {data['city']}")

            except KeyError as err:
                print(err)

        return data_list
