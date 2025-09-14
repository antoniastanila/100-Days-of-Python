import requests
import datetime
import os

APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
API_KEY = os.environ.get("NUTRITIONIX_APP_KEY")
nutritionix_endpoint = os.environ.get("NUTRITIONIX_ENDPOINT")
sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")
TOKEN = os.environ.get("BEARER_TOKEN")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": input("Tell me which exercises you did: "),
    "weight_kg": input("How much do you weigh: "),
    "height_cm": input("How tall are you (in cm): "),
    "age": input("Last but not least, how old are you: ")
}

response = requests.post(url=nutritionix_endpoint,
                         json=parameters, headers=headers)
data = response.json()["exercises"]
print(response.text)

bearer_headers = {
    "Authorization": TOKEN
}

for index in range(len(data)):
    row_contents = {
        "workout": {
            "date": str(datetime.datetime.now().strftime("%d/%m/%Y")),
            "time": str(datetime.datetime.now().strftime("%H:%M:%S")),
            "exercise": data[index]["user_input"].title(),
            "duration": data[index]["duration_min"],
            "calories": data[index]["nf_calories"]
        }
    }

    response = requests.post(
        url=sheety_endpoint, json=row_contents, headers=bearer_headers)
    print(response.text)
