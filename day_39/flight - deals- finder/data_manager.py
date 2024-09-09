import requests
from  flight_data import *
import os

proxy = {                                        #* proxies=proxy) in case u need intel proxy
    'http': 'http://proxy-chain.intel.com:911',
    'https': 'http://proxy-chain.intel.com:912',
}

# class to handle the data in exel
class DataManager:

    def __init__(self):
        self.end_point = "https://api.sheety.co/3d22c46a86d5caef41b2a5f071fd1415/flightDeals/prices"
        self.data = requests.get(url=self.end_point, proxies=proxy).json()


    def get_ata_code(self):

        for index in self.data['prices']:  #  we will need index to be number to enter row by row
            print(index)
            if index["iataCode"] == "":     # in case we need to find the iata to put in the row
                self.flight_data =           # here we will put the block to update the empty slot


                info = requests.put(url=self.end_point + f"/{index['id']}",
                                    headers={'Content-Type': 'application/json'}, json=data, proxies=proxy)

            else:

                data = {
                     "price": {
                        "iataCode": "Test"

                     }}

                info = requests.put(url=self.end_point+f"/{index['id']}", json=data , proxies=proxy)

                print(info.text)
