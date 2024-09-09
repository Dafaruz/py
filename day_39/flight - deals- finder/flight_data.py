import requests
from flight_search import  FlightSearch
proxy = {                                        #* proxies=proxy) in case u need intel proxy
    'http': 'http://proxy-chain.intel.com:911',
    'https': 'http://proxy-chain.intel.com:912',
}

# class that will handel the data


class FlightData:
        def __init__(self,):
                self.end_point = "https://test.api.amadeus.com/v1/reference-data/locations"  # end point for search
                self.data = {

                       "subType ": "CITY&keyword",
                       "view": "LIGHT ",
                       "keyword ": "LON"
                }

        def fill_empty_ata_code(self,city_data):

                header = {"Authorization":" Bearer CpjU0sEenniHCgPDrndzOSWFk5mN"}
                for city in city_data:

                    city['iataCode']

                    data = requests.get(url= self.end_point, headers=header, data=self.subType ,proxies=proxy).json() # will return data on a city name so we can get ata code
