import requests
import os


class FlightSearch:

    def __init__(self):
        self.data = requests.get(url="https://api.sheety.co/3d22c46a86d5caef41b2a5f071fd1415/flightDeals/prices").json()
        self.api_key = os.environ.get("AMADEUS_API_KEY")
        self.api_secret = os.environ.get("AMADEUS_API_SECRET")
        print(self.api_key,self.api_secret)
        self._token = self._get_new_token()

    def _get_new_token(self):
        header = {
            "content-type": "application/x-www-form-urlencoded"
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": "ZVAS579clKVntZbgsubQdHmFhIHG1cxu",
            "client_secret": "RAxwj93Os3mzGxYG"
        }
        print(body)
        data = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token", headers=header, data=body).json()
        print(f"your generate token is{data['access_token']}\n")
        print(f"pls notice this token will end in {data['expires_in']} sec")

        return data['access_token']

