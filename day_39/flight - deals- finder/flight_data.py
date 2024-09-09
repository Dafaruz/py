
import requests

proxy = {  # * proxies=proxy) in case u need intel proxy
    'http': 'http://proxy-chain.intel.com:911',
    'https': 'http://proxy-chain.intel.com:912',
}


class FlightData:
    def __init__(self, token):
        self.end_point = "https://test.api.amadeus.com/v1/reference-data/locations/cities"  # end point for search
        self.token = token
        self.data = {
            "keyword": "Test"
        }
        self.header = {"Authorization": f"Bearer {self.token}",
                       "accept": "application/vnd.amadeus+json"}

    def find_ata_code(self, city):
        self.data['keyword'] = city

        data = requests.get(url=self.end_point, headers=self.header, params=self.data).json()  # get ata code

        try:
            return data['data'][0]["iataCode"]        # try to return the right ata code

        except KeyError as x:
            print(x)
