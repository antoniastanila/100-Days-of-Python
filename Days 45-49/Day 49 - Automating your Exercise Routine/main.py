import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.common.keys import Keys

load_dotenv()

GYM_URL = os.getenv("GYM_URL")
ACCOUNT_EMAIL = os.getenv("ACCOUNT_EMAIL")
ACCOUNT_PASSWORD = os.getenv("ACCOUNT_PASSWORD")

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)

driver.get(GYM_URL)

# ============================= AUTOMATED LOGIN =============================

wait = WebDriverWait(driver, 2)

login_button = wait.until(
    ec.element_to_be_clickable(By.ID, value="login-button"))
login_button.click()

email_input = wait.until(
    ec.element_to_be_clickable(By.ID, value="email-input"))
email_input.clear()
email_input.send_keys(ACCOUNT_EMAIL)

password_input = driver.find_element(By.ID, value="password-input")
password_input.clear()
password_input.send_keys(ACCOUNT_PASSWORD)

submit_button = driver.find_element(By.ID, value="submit-button")
submit_button.click()

# ??? Wait for schedule page to load
wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))
