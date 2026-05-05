import os
from time import time, sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

load_dotenv()

URL = os.getenv("COOKIE_URL")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

sleep(3)

lang_button = driver.find_element(By.ID, value="langSelect-EN")
lang_button.click()

sleep(3)

cookie_button = driver.find_element(By.ID, value="bigCookie")

power_up = {}
product0 = driver.find_element(By.ID, value="product0")
product1 = driver.find_element(By.ID, value="product1")

power_up[product0] = int(driver.find_element(
    By.ID, value="productPrice0").text)

power_up[product1] = int(driver.find_element(
    By.ID, value="productPrice1").text)

print(power_up)
number_of_cookies = driver.find_element(By.XPATH, value='//*[@id="cookies"]')
print(number_of_cookies.text.split())

timeout = time() + 60 * 5
next_check = time() + 5

while True:
    if time() > timeout:
        break
    if len(power_up) != 4:
        if int(number_of_cookies.text.split()[0]) >= power_up[product0]:
            product2 = driver.find_element(By.ID, value="product2")
            power_up[product2] = driver.find_element(
                By.ID, value="productPrice2").text
        elif int(number_of_cookies.text.split()[0]) >= power_up[product1]:
            product3 = driver.find_element(By.ID, value="product3")
            power_up[product3] = driver.find_element(
                By.ID, value="productPrice3").text
    index = 0
    for key in power_up:
        if key.get_attribute("class") != "product unlocked enabled":
            break
        compare_with = int(driver.find_element(
            By.ID, value=f"productPrice{index}").text.replace(",", ""))
        if power_up[key] < compare_with:
            power_up[key] = compare_with
        index += 1

    if time() > next_check:
        print("5 sec")
        next_check += 5
        for key in reversed(power_up):
            if key.get_attribute("class") == "product unlocked enabled":
                key.click()
                break
    cookie_button.click()

sleep(3)

cookies_per_second = driver.find_element(
    By.ID, value="cookiesPerSecond").text.split()[2]
print(f"Total number of cookies per second: {cookies_per_second}")
