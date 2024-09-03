import requests
import urllib3
from datetime import datetime as datetime
TOKEN = "5G4Z1(b)uv1q)"
USER_NAME = "dfaruz"
headers = {'Content-Type': 'application/json; charset=utf-8'}


current_date = datetime.now()

# Format the date as yyyyMMdd
formatted_date = current_date.strftime("%Y%m%d")



url = "https://pixe.la/v1/users"

proxies = {
    'http': 'http://proxy-chain.intel.com:911',
    'https': 'http://proxy-chain.intel.com:912',
}

graph_endpoint = f"{url}/{USER_NAME}/graphs"

parameters_of_user = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"}

graph_header = {
    "X-USER-TOKEN": TOKEN
}

graph_body = {
    "id": "graph1",
    "name": "coding",
    "unit": "hours",
    "type": "int",
    "color": "sora"
}

# response = requests.post(url=url, json=parameters_of_user, headers=headers, proxies=proxies)
# print(response.text)

# response from server{"message":"Success. Let's visit https://pixe.la/@dfaruz ,
# it is your profile page!","isSuccess":true}  so now we have the user and we will need to hide our token



# response = requests.post(url=graph_endpoint, json=graph_body, headers=graph_header, proxies=proxies)
#
# print(response.text)

graph_update = {
    "date": formatted_date,
    "quantity": "2",
}

graph1_endpoint = f"{url}/{USER_NAME}/graphs/graph1"

update = requests.put(url=graph1_endpoint, headers=graph_header, proxies=proxies, json=graph_update)
print(update.text)