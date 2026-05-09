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

# ============================= Automated Login =============================

wait = WebDriverWait(driver, 2)

login_button = wait.until(
    ec.element_to_be_clickable((By.ID, "login-button")))
login_button.click()

email_input = wait.until(
    ec.element_to_be_clickable((By.ID, "email-input")))
email_input.clear()
email_input.send_keys(ACCOUNT_EMAIL)

password_input = driver.find_element(By.ID, value="password-input")
password_input.clear()
password_input.send_keys(ACCOUNT_PASSWORD)

submit_button = driver.find_element(By.ID, value="submit-button")
submit_button.click()

# ??? Wait for schedule page to load
wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

# ===================== Book the upcoming Tuesday class =====================

cards_list = driver.find_elements(
    By.CSS_SELECTOR, value="div[id^='class-card-']")

for card in cards_list:
    time = card.find_element(By.CSS_SELECTOR, value="p[id^='class-time']")
    if time.text == "Time: 6:00 PM":
        parent_div = card.find_element(
            By.XPATH,
            "./ancestor::div[starts-with(@id, 'day-group-')][1]"
        )
        day = parent_div.find_element(By.TAG_NAME, value="h2").text

        if '(Tue' in day.split() or 'Tue,' in day.split():
            book_button = card.find_element(
                By.CSS_SELECTOR, value="button[id^='book-button-']")
            class_name = card.find_element(
                By.CSS_SELECTOR, value="h3[id^='class-name-']").text
            try:
                book_button.click()
            except:
                print("Couldn't book class!")
            else:
                if 'Tue,' in day.split():
                    print(
                        f"✓ Booked: {class_name} on Tue, {day.split()[1]} {day.split()[2]}")
                elif '(Tue' in day.split():
                    print(
                        f"✓ Booked: {class_name} on Tue, {day.split()[2]} {day.split()[3].replace(")", "")}")
            finally:
                break


# REFA PARTEA ASTA FACAND LISTA CU CARDURILE IN LOCUL CELOR DOUA LISTE CU TIME SI BUTTONS !!
