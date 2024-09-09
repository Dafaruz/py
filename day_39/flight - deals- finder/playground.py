from datetime import datetime, timedelta
import  requests

x= (datetime.now()+timedelta(days=5)).strftime("%Y-%m-%d")
print(x)
x=datetime.now().weekday()
print(type(x))
end_point = "https://api.sheety.co/3d22c46a86d5caef41b2a5f071fd1415/flightDeals/prices"
data = requests.get(url=end_point).json()
for i in data['prices']:
    print(i)
