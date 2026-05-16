import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep
load_dotenv()

TWITTER_URL = "https://x.com/"
SPEEDTEST_URL = "https://www.speedtest.net/"
PROMISED_DOWN = os.getenv("PROMISED_DOWN")
PROMISED_UP = os.getenv("PROMISED_UP")


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(url=SPEEDTEST_URL)

        try:
            reject_button = self.wait.until(ec.element_to_be_clickable((
                By.CSS_SELECTOR, "button#onetrust-reject-all-handler")))
            reject_button.click()
        except (TimeoutException, NoSuchElementException):
            print("Did not get Cookie popup!")

        go_button = self.wait.until(ec.element_to_be_clickable(
            (By.CSS_SELECTOR, "span.start-text")))
        go_button.click()

        self.down = self.wait.until(ec.element_to_be_clickable(
            (By.CSS_SELECTOR, "span.download-speed")))
        self.down = self.down.text
        self.up = self.wait.until(ec.element_to_be_clickable(
            (By.CSS_SELECTOR, "span.upload-speed")))
        self.up = self.up.text

        while self.down == "—":
            sleep(5)
            self.down = self.driver.find_element(
                By.CSS_SELECTOR, value="span.download-speed").text
        while self.up == "—":
            sleep(5)
            self.up = self.driver.find_element(
                By.CSS_SELECTOR, value="span.upload-speed").text

        print(f"down: {self.down}\nup: {self.up}")

    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)
        input_box = self.wait.until(ec.presence_of_element_located(
            (By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')))

        input_box.send_keys(
            f"Hi!\nMy internet speed is {self.down}down/{self.up}up and I pay for {PROMISED_DOWN}down/{PROMISED_UP}up. Amazing!")

        post_button = self.driver.find_element(
            By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/button')
        post_button.click()


little_botty = InternetSpeedTwitterBot()
little_botty.get_internet_speed()
little_botty.tweet_at_provider()
