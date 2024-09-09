import requests
from flight_data import FlightData

import os

proxy = {                                        #* proxies=proxy) in case u need intel proxy
    'http': 'http://proxy-chain.intel.com:911',
    'https': 'http://proxy-chain.intel.com:912',
}

# class to handle the data in exel
class DataManager:

    def __init__(self, flight_data: FlightData):
        self.end_point = "https://api.sheety.co/3d22c46a86d5caef41b2a5f071fd1415/flightDeals/prices"
        self.data = requests.get(url=self.end_point).json()
        self.missing_ata_list = []
        self.flight_data = flight_data

    def check_ata_status(self):

        for index in self.data['prices']:  #  we will need index to be number to enter row by row
            if index["iataCode"] == "":     # in case we need to find the iata to put in the row
                self.missing_ata_list.append(index['city'])
                fixed_value = self.flight_data.find_ata_code(index['city'])

                new_data = {
                    "price": {
                        "iataCode": fixed_value
                    }
                }
                info = requests.put(url=self.end_point + f"/{index['id']}",
                                      headers={'Content-Type': 'application/json'}, json=new_data,)


                print(info.text)
        print(f"the missing cities list is : {self.missing_ata_list}")


