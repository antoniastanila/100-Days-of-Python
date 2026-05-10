import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException

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

# ===================== Book the upcoming Tuesday and Thursday 6PM classes =====================

cards_list = driver.find_elements(
    By.CSS_SELECTOR, value="div[id^='class-card-']")

# Counters
new_bookings = 0
new_waitlist = 0
already_booked_or_waitlisted = 0

processed_classes = []

for card in cards_list:
    time = card.find_element(By.CSS_SELECTOR, value="p[id^='class-time']")
    if time.text == "Time: 6:00 PM":
        parent_div = card.find_element(
            By.XPATH,
            "./ancestor::div[starts-with(@id, 'day-group-')][1]"
        )
        day = parent_div.find_element(By.TAG_NAME, value="h2").text

        if 'Tue' in day or 'Thu' in day:
            book_button = card.find_element(
                By.CSS_SELECTOR, value="button[id^='book-button-']")
            class_name = card.find_element(
                By.CSS_SELECTOR, value="h3[id^='class-name-']").text

# ===================== Checking if class already booked =====================

            class_info = f"{class_name} on {day}"

            if book_button.text == "Book Class":
                book_button.click()
                new_bookings += 1
                processed_classes.append(f"[New Booking]: {class_info}")
                print(
                    f"✓ Booked: {class_info}")

            elif book_button.text == "Booked":
                already_booked_or_waitlisted += 1
                print(
                    f"✓ Already booked: {class_info}")

            elif book_button.text == "Join Waitlist":
                book_button.click()
                new_waitlist += 1
                print(
                    f"✓ Joined waitlist for: {class_info}")
                processed_classes.append(f"[New Waitlist]: {class_info}")

            elif book_button.text == "Waitlisted":
                already_booked_or_waitlisted += 1
                print(
                    f"✓ Already on waitlist: {class_info}")


# ===================== Booking Summary =====================

total_classes_processed = sum(
    (new_bookings, new_waitlist, already_booked_or_waitlisted))

# print(f"""--- BOOKING SUMMARY ---
# Classes booked: {new_bookings}
# Waitlists joined: {new_waitlist}
# Already booked/waitlisted: {already_booked_or_waitlisted}
# Total Tuesday & Thursday 6PM classes processed: {total_classes_processed}""")

# print("\n--- DETAILED CLASS LIST ---")
# for class_detail in processed_classes:
#     print(f"  • {class_detail}")

# ===================== Checking My Bookings Page =====================

print(f"--- Total Tuesday/Thursday 6pm classes: {total_classes_processed} ---")

print("--- VERIFYING ON MY BOOKINGS PAGE ---")

driver.find_element(By.LINK_TEXT, value="My Bookings").click()

try:
    confirmed_bookings = driver.find_elements(
        By.CSS_SELECTOR, value="div[id^='booking-card-']")
except NoSuchElementException:
    print("Did not find any confirmed bookings!")
else:
    for element in confirmed_bookings:
        class_info = element.find_element(By.TAG_NAME, value="h3")
        print(f"✓ Verified: {class_info.text}")

try:
    waitlists = driver.find_elements(
        By.CSS_SELECTOR, value="div[id^='waitlist-card-']")
except NoSuchElementException:
    print("Did not find any waitlists!")
else:
    for element in waitlists:
        class_info = element.find_element(By.TAG_NAME, value="h3")
        print(f"✓ Verified: {class_info.text}")

print("--- VERIFICATION RESULT ---")

expected = sum((new_bookings, new_waitlist, already_booked_or_waitlisted))
found = len(confirmed_bookings) + len(waitlists)

print(f"Expected: {expected}")
print(f"Found: {found}")

if expected == found:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(
        f"❌ MISMATCH: Missing {total_classes_processed - expected - found} bookings")
