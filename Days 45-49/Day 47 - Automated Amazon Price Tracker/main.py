import os
import requests
import smtplib
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

TARGET_PRICE = 100
SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
MY_EMAIL = os.getenv("EMAIL_ADDRESS")
MY_PASSWORD = os.getenv("EMAIL_PASSWORD")
URL = os.getenv("DESIRED_PRODUCT")
header = {
    "Accept-Language": "ro-RO,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,ro;q=0.6,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
}

res = requests.get(url=URL, headers=header)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

whole_price = soup.select_one(".a-price-whole")
fraction_price = soup.select_one(".a-price-fraction")

price = whole_price.text + fraction_price.text

price = float(price)
print(price)

# ====================== Sending an Email ===========================

product_title = soup.find(id="title").get_text().strip()

print(product_title)

if price < TARGET_PRICE:
    message = f"{product_title} is on sale for only {price} !!!"

    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8"))
