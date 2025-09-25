from flight_search import FlightSearch
from pprint import pprint
from data_manager import DataManager
import datetime
import time

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_data()

start = datetime.date.today() + datetime.timedelta(days=1)
end = start + datetime.timedelta(days=180)

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.populate_iata_column(row["city"])
        data_manager.put_data(row)
else:
    for row in sheet_data:
        print(f"Getting flights for {row['city']}...")
        smallest_price = flight_search.search_for_flights(
            row["city"], row["iataCode"])
        data_manager.compare_prices(
            row["city"], smallest_price, flight_search._tomorrow_date)
