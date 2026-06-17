import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

load_dotenv()

ZILLOW_URL = os.getenv("ZILLOW_URL")

response = requests.get(url=ZILLOW_URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

listings = soup.find_all(class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

links = []
prices = []
addresses = []

for card in listings:
    links.append(card.find("a").get("href"))
    prices.append(card.find(
        class_="PropertyCardWrapper__StyledPriceLine").text.strip(" +/mo1bd"))
    addresses.append(card.find("address").text.strip(" \n").replace("|", ","))

# print(links)
# print(prices)
# print(addresses)
