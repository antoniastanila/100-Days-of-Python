import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()

URL = os.getenv("DESIRED_URL")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# price_ron = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_coins = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text

# print(f"The price: {price_ron}.{price_coins} RON")

search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("class"))

button = driver.find_element(By.ID, value="submit")
print(button.size)

documentation_link = driver.find_element(
    By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

bug_link = driver.find_element(
    By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

# ============================= SCRAPING UPCOMING EVENTS FROM PYTHON =============================

upcoming_events = {}

times_list = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
times_list = [time.text for time in times_list]
print(times_list)

names_list = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
names_list = [name.text for name in names_list]
print(names_list)

upcoming_events = {index:  {
    'time': times_list[index], 'name': names_list[index]} for index in range(len(times_list))}

print(upcoming_events)

# driver.close() # this only closes the current tab
driver.quit()    # while this closes the entire program, shuts down the entire browser
