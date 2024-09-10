from datetime import datetime, timedelta
import  requests
proxy = {  # * proxies=proxy) in case u need intel proxy
    'http': 'http://proxy-chain.intel.com:911',
    'https': 'http://proxy-chain.intel.com:912',
}
x= (datetime.now()+timedelta(days=5)).strftime("%Y-%m-%d")
print(x)
x=datetime.now().weekday()
print(x)
end_point = "https://api.sheety.co/3d22c46a86d5caef41b2a5f071fd1415/flightDeals/prices"
data = requests.get(url=end_point).json()

print(data)