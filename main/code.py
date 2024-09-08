import os
import requests
from datetime import datetime

APP_ID = os.environ["API_ID"]
API_KEY = os.environ["API_KEY"]
GENDER = "male"
WEIGHT = 75
HEIGHT = 162.56
AGE = 33

excercise_endpoint = os.environ["EX_END"]
sheety_endpoint = os.environ["SHT_END"]

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

bearer_headers = {
    "Authorization": os.environ["BEAR_AUTH"]
}

parameters = {
    "query": input("Which exercise you did today: "),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=excercise_endpoint, json=parameters, headers= headers)
result = response.json()

current_date = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_parameters = {
        "sheet1": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url= sheety_endpoint, json= sheet_parameters, headers= bearer_headers)
    print(sheet_response.text)
