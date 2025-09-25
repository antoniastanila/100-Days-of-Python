import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_PRICES_ENDPOINT")
ORIGIN_CODE = os.getenv("ORIGIN_CODE")


class DataManager:
    def __init__(self):
        self._token = os.getenv("SHEETY_TOKEN")
        self.headers = {
            "Authorization": self._token
        }

    def get_data(self):
        response = requests.get(
            url=SHEETY_PRICES_ENDPOINT, headers=self.headers)
        data = response.json()["prices"]
        return data

    def put_data(self, row):
        prices_put_endpoint = f"{SHEETY_PRICES_ENDPOINT}/{row['id']}"
        contents = {
            "price": {
                "iataCode": row["iataCode"]
            }
        }
        response = requests.put(url=prices_put_endpoint,
                                json=contents, headers=self.headers)
        return response.json()

    def compare_prices(self, city, smallest_price, date):
        data = self.get_data()
        for piece in data:
            if piece["city"] == city:
                price_from_sheet = piece["lowestPrice"]
                destination_code = piece["iataCode"]
                break
        try:
            if price_from_sheet > float(smallest_price):
                with open("file.txt", "a") as data_file:
                    data_file.write(
                        f"Low price alert! Only £{smallest_price} to fly from {ORIGIN_CODE} to {destination_code} on {date}\n\n")
        except ValueError:
            pass
