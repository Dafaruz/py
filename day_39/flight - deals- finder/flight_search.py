import requests
import os

proxy = {

    'http': 'http://proxy-chain.intel.com:911',
    'https': 'http://proxy-chain.intel.com:912',
}
# class to search for data in the api


class FlightSearch:

    def __init__(self):
        self.api_key = os.environ.get("AMADEUS_API_KEY")
        self.api_secret = os.environ.get("AMADEUS_API_SECRET")
        self.token = self.get_new_token()

    def get_new_token(self):

        header = {

            "content-type": "application/x-www-form-urlencoded"
        }

        body = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }

        data = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token", headers=header,
                             data=body, proxies=proxy).json()

        print(f"your generate token is{data['access_token']}\n")
        print(f"pls notice this token will end in {data['expires_in']} sec")

        return data['access_token']




