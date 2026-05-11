import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
load_dotenv()

URL = os.getenv("TINDER_URL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
MY_EMAIL = os.getenv("MY_EMAIL")

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)


time.sleep(2)
login_button = driver.find_element(By.LINK_TEXT, value="Log in")
login_button.click()

time.sleep(2)
google_button = driver.find_element(
    By.CSS_SELECTOR, value="#t-671667020 .S9gUrf-YoZ4jf")
google_button.click()

time.sleep(6)
email_input = driver.find_element(By.XPATH, value='//*[@id="identifierId"]')
email_input.send_keys(MY_EMAIL, Keys.ENTER)
