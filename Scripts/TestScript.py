import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import yaml


# Start Firefox WebDriver
driver = webdriver.Firefox()
# Open the Coursera page
driver.get("https://www.coursera.org/professional-certificates/google-cybersecurity")


def type_slowly(element, text):
    for char in text:
        element.send_keys(char)
        Random_Time_Delay()

def Random_Time_Delay():
    time.sleep(random.uniform(0.3, 1.5))
    
# Wait for the page to load
Random_Time_Delay()

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
Random_Time_Delay()
FinancialAidBtn.click()

# Put User Account Info for login
Random_Time_Delay()
EmailField = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#email'))
)
type_slowly(EmailField, user_data["email"])

PasswordField = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#password'))
)
type_slowly(PasswordField, user_data["password"])
# Sleep to simulate human-like interaction
Random_Time_Delay()

LoginBtn = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "._6dgzsvq"))
)
LoginBtn.click()
Random_Time_Delay()

FinancialAidBtn.click()
Random_Time_Delay()


# Get the total number of courses available
total_courses = len(driver.find_elements_by_css_selector(".cui-isChecked > input"))
Random_Time_Delay()
# Generate a random course number between 1 and total_courses
course_number = random.randint(1, total_courses)

CourseSelect = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, f".cui-isChecked > input:nth-child({course_number})"))
)
Random_Time_Delay()
# Quit the WebDriver
driver.quit()
