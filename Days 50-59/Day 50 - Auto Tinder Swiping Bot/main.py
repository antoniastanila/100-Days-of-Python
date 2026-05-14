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

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

wait = WebDriverWait(driver, 10)


# LOGIN WORKFLOW COMMENTED BECAUSE GOOGLE DOESN'T ALLOW BOTS TO INTRODUCE PASSWORDS DUE TO SECURITY REASONS

# login_button = wait.until(
#     ec.element_to_be_clickable((By.LINK_TEXT, "Log in"))
# )

# login_button.click()

# google_iframe = wait.until(ec.presence_of_element_located(
#     (By.CSS_SELECTOR, "iframe[src*='accounts.google.com/gsi/button']")
# ))
# driver.switch_to.frame(google_iframe)

# google_button = wait.until(
#     ec.element_to_be_clickable((By.CSS_SELECTOR, "div[role='button']"))
# )
# google_button.click()

# driver.switch_to.default_content()

# driver.switch_to.window(driver.window_handles[-1])

# email_input = wait.until(ec.presence_of_element_located(
#     (By.CSS_SELECTOR, "input[type='email']")))
# email_input.send_keys(MY_EMAIL, Keys.ENTER)

for index in range(100):
    try:
        dislike_button = wait.until(ec.element_to_be_clickable(
            (By.XPATH, '//*[@id="main-content"]/div[1]/div/div/div/div[1]/div/div/div[4]/div/div[2]/button')))
        dislike_button.click()
        time.sleep(2)
    except TimeoutException:
        print("Had a little issue there... oops")
        driver.save_screenshot(f"timeout_{index}.png")
        break

# print(driver.window_handles)
