import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

load_dotenv()

ZILLOW_URL = os.getenv("ZILLOW_URL")

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,fr-FR;q=0.9,fr;q=0.8,ro-RO;q=0.7,ro;q=0.6,en;q=0.5"
}

response = requests.get(url=ZILLOW_URL, headers=header)
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
