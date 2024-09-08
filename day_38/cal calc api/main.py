import requests
import datetime
API_KEY = "6b9a51a5ea2cb451edbe6720cabf51d3"
USER_ID = "88be1774"

END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
WEIGHT = 92
HEIGHT = 176
AGE = 34
EXEL_END_POINT = "https://api.sheety.co/3d22c46a86d5caef41b2a5f071fd1415/myWorkouts/workouts"

proxy = {
    'http': 'http://proxy-chain.intel.com:911',
    'https': 'http://proxy-chain.intel.com:912',
}

header = {
    "x-app-id": USER_ID,
    "x-app-key": API_KEY

}

body = {
    "query": input("what is your drug"),
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}
data = requests.post(url=END_POINT, json=body, proxies=proxy, headers=header)

info_j = data.json()


date = datetime.datetime.now().strftime("%d/%m/%Y")
time = datetime.datetime.now().strftime("%X")

for exercise in info_j["exercises"]:

    sheet_workout = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["user_input"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]

        }
    }

status = requests.post(EXEL_END_POINT, json=sheet_workout, proxies=proxy)
print(status.text)