import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep
load_dotenv()

INSTA_URL = os.getenv("INSTA_URL")


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)

        self.username = os.getenv("INSTA_USERNAME")
        self.password = os.getenv("INSTA_PASSWORD")
        self.popup = ''

    def login(self):
        self.driver.get(url=INSTA_URL)

        try:
            decline_cookies_button = self.wait.until(
                ec.element_to_be_clickable((By.CSS_SELECTOR, 'button._a9--')))
            decline_cookies_button.click()
        except:
            print("Did not find button to decline cookies.")

        username_input = self.wait.until(ec.element_to_be_clickable((
            By.XPATH, '//*[@id="_R_c9d9lplcldcpbn6b5ipamH1_"]')))
        username_input.send_keys(self.username, Keys.ENTER)

        password_input = self.wait.until(ec.element_to_be_clickable(
            (By.XPATH, '//*[@id="_R_cdd9lplcldcpbn6b5ipamH1_"]')))
        password_input.send_keys(self.password, Keys.ENTER)

    def find_followers(self):
        target_insta_url = INSTA_URL + os.getenv("TARGET_ACCOUNT") + "/"
        print(target_insta_url)
        self.driver.get(url=target_insta_url)

        followers = self.wait.until(
            ec.element_to_be_clickable(
                (By.XPATH, "//span[contains(., 'followers')]")
            )
        )

        followers.click()

        self.popup = self.wait.until(ec.presence_of_element_located(
            (By.XPATH, "//div[@role='dialog']")))
        sleep(3)
        # elem_inside_popup = self.popup.find_element(By.XPATH, ".//a")
        # elem_inside_popup.send_keys(Keys.END)

    def follow(self):
        follow_buttons = self.popup.find_elements(
            By.XPATH, ".//button[contains(., 'Follow')]")
        for button in follow_buttons:
            if button.text.strip() != 'Follow':
                continue
            button.click()
            sleep(5)


follower_botty = InstaFollower()
# follower_botty.login()
follower_botty.find_followers()
follower_botty.follow()
