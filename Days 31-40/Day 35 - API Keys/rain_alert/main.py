import requests

app_key = "8339798330565dec04b39b480ac33ca3"

parameters = {
    "lat": 44.926901,
    "lon": 25.457324,
    "appid": app_key,
    "cnt": 4
}


response = requests.get(
    url=" https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
print(weather_data)

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        print("Bring an umbrella!")
