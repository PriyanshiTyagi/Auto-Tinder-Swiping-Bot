from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

import os
from dotenv import load_dotenv

load_dotenv()

MAIL = os.getenv("FACEBOOK_MAIL")
PASSWORD = os.getenv("FACEBOOK_PASSWORD")

driver = webdriver.Chrome()
driver.get("https://tinder.com/")
driver.maximize_window()
time.sleep(4)

# clicking on log in button

driver.find_element(By.XPATH,
                    '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]').click()
time.sleep(4)
try:
    # clicking on LOG IN WITH FACEBOOK

    driver.find_element(By.XPATH,
                        '/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]').click()

except:
    time.sleep(4)
    # trying to find MORE OPTIONS button as
    driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/button').click()
    print("Clicked")

    # again clicking on LOG IN WITH FACEBOOK

    driver.find_element(By.XPATH,
                        '/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]').click()

time.sleep(4)

# switching to popped up facebook window

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

time.sleep(4)

# inputing the mail and password

driver.find_element(By.NAME, "email").send_keys(MAIL)
driver.find_element(By.NAME, "pass").send_keys(PASSWORD)
time.sleep(4)
driver.find_element(By.NAME, "login").click()
time.sleep(4)

# switching to base window
driver.switch_to.window(base_window)
print(driver.title)

# Click ALLOW for location.
time.sleep(20)
driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]').click()

# Click NOT INTERESTED for notifications.
time.sleep(4)
driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[2]/div[2]/div[2]').click()

# Click I ACCEPT for cookies
time.sleep(4)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]').click()

time.sleep(4)

for n in range(10):

    # Add a 1 second delay between likes.
    time.sleep(1)

    try:
        print("called")

        body = driver.find_element(By.CSS_SELECTOR, 'body')
        body.send_keys(Keys.RIGHT)

    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)
time.sleep(10)
