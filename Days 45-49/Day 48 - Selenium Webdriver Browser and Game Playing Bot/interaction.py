import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()

URL = os.getenv("OTHER_URL")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# # all_portals.click()

fname = driver.find_element(By.NAME, value="fName")
lname = driver.find_element(By.NAME, value="lName")
e_address = driver.find_element(By.NAME, value="email")

submit_button = driver.find_element(By.CLASS_NAME, value="btn")

fname.send_keys("Anto")
lname.send_keys("Nia")
e_address.send_keys("antoniamaria.stanila@gmail.com")

e_address.send_keys(Keys.ENTER)

# driver.quit()
