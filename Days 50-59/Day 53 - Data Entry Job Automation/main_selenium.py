from main_bs import links, prices, addresses
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
load_dotenv()

FORM_URL = os.getenv("GOOGLE_FORM_URL")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(FORM_URL)
wait = WebDriverWait(driver, 10)

for index in range(len(links)):
    address_input = wait.until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    address_input.send_keys(addresses[index])

    price_input = wait.until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    price_input.send_keys((prices[index]))

    link_input = wait.until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    link_input.send_keys(links[index])

    sumbit_button = driver.find_element(
        By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    sumbit_button.click()
    next_response = wait.until(ec.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')))
    next_response.click()
