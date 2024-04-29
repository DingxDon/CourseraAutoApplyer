from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import yaml
import time
import random






# Start Firefox WebDriver
driver = webdriver.Firefox()
# Open the Coursera page
driver.get("https://www.coursera.org/professional-certificates/google-cybersecurity")


def type_slowly(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))


# Wait for the page to load
time.sleep(2)

# Load user data from YAML file
with open(r"Scripts\Data\credentials.yaml", 'r') as c:
    user_data = yaml.safe_load(c)

# Get Course Name from Site
CourseName = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'h1.cds-119:nth-child(2)'))
)
print("Course Name: ", CourseName.text)

# Find Financial Aid Button and Click it to start the process
FinancialAidBtn = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.button-link'))
)
time.sleep(1)
FinancialAidBtn.click()

# Put User Account Info for login
time.sleep(1)
EmailField = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#email'))
)
type_slowly(EmailField, user_data["email"])

PasswordField = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#password'))
)
type_slowly(PasswordField, user_data["password"])
# Sleep to simulate human-like interaction
time.sleep(1)

LoginBtn = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "._6dgzsvq"))
)
LoginBtn.click()
time.sleep(3)


# Quit the WebDriver
driver.quit()
