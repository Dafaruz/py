import requests
import datetime
import os

API_KEY_nutritionix = os.environ.get("API_KEY_nutritionix")
USER_ID_nutritionix = os.environ.get("USER_ID_nutritionix")


END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
WEIGHT = 92
HEIGHT = 176
AGE = 34
EXEL_END_POINT = "https://api.sheety.co/3d22c46a86d5caef41b2a5f071fd1415/myWorkouts/workouts"

proxy = {                                        #* proxies=proxy) in case u need intel proxy
    'http': 'http://proxy-chain.intel.com:911',
    'https': 'http://proxy-chain.intel.com:912',
}

header = {
    "x-app-id": USER_ID_nutritionix,
    "x-app-key": API_KEY_nutritionix
}

body = {
    "query": input("what is your drug"),
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}
data = requests.post(url=END_POINT, json=body, headers=header)
info_j = data.json()

date = datetime.datetime.now().strftime("%d/%m/%Y")
time = datetime.datetime.now().strftime("%X")
print(info_j)
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

status = requests.post(EXEL_END_POINT, json=sheet_workout)
print(status.text)
