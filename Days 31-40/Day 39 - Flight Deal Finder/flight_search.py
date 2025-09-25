from dotenv import load_dotenv
import os
import datetime
import requests
from flight_data import find_cheapest_flight
load_dotenv()


class FlightSearch:
    def __init__(self):
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._api_secret = os.getenv("AMADEUS_API_SECRET")
        self._token = self._get_new_token()
        self._tomorrow_date = datetime.date.today() + datetime.timedelta(days=1)

    def populate_iata_column(self, city_name):
        search_cities_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        params = {
            "keyword": city_name
        }
        header = {
            "Authorization": f"Bearer {self._token}"
        }
        response = requests.get(
            url=search_cities_endpoint, headers=header, params=params)
        response.raise_for_status()
        code = response.json()["data"][0]["iataCode"]
        return code

    def _get_new_token(self):
        authorization_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }

        response = requests.post(
            authorization_endpoint, data=body, headers=headers)
        return response.json()["access_token"]

    def search_for_flights(self, city, code, dep_date=None):
        search_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        header = {
            "Authorization": f"Bearer {self._token}"
        }
        dep = dep_date if dep_date else self._tomorrow_date
        params = {
            "originLocationCode": os.getenv("ORIGIN_CODE", "LON"),
            "destinationLocationCode": code,
            "departureDate": f"{self._tomorrow_date:%Y-%m-%d}",
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP"
        }
        try:
            response = requests.get(url=search_endpoint,
                                    headers=header, params=params)
            response.raise_for_status()
            flight_offers = response.json()["data"]
            cheapest_flight = find_cheapest_flight(flight_offers)
            price_str = cheapest_flight["price"]["total"] if cheapest_flight else None
            price = float(price_str) if price_str is not None else None
        except (requests.RequestException, KeyError, ValueError):
            price = None
        print(f"{city} {dep:%Y-%m-%d}: £{price if price else 'N/A'}")
        return price
