import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import yaml


class CourseraBot:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 10)
        self.user_data = self.load_user_data()

    def locate_element_by_css(self, css_selector):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

    def type_slowly(self, element, text):
        for char in text:
            element.send_keys(char)
            time.sleep(random.uniform(0.1, 0.5))

            # Introduce random delays after punctuation
            if char in '.?!' and random.random() < 0.2:
                pause_duration = random.uniform(0.5, 1.5)
                time.sleep(pause_duration)

    # Function to simulate human-like slow page surfing (clicking)
    def Random_Time_Delay(self):
        time.sleep(random.uniform(0.3, 1.5))

    def load_user_data(self):
        with open(r"Scripts\Data\credentials.yaml", 'r') as c:
            user_data = yaml.safe_load(c)
        return user_data

    def Course(self):
        self.driver.get(
            "https://www.coursera.org/professional-certificates/google-cybersecurity")

        self.Random_Time_Delay()

        CourseName = self.locate_element_by_css('h1.cds-119:nth-child(2)')

        print("Course Name: ", CourseName.text)

        time.sleep(30)
        FinancialAidBtn = self.locate_element_by_css('.button-link')

        FinancialAidBtn.click()
        
        """self.Random_Time_Delay()

        FinancialAidBtn.click()

        self.Random_Time_Delay()

        EmailField = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#email')))

        self.type_slowly(EmailField, self.user_data["email"])

        PasswordField = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#password')))

        self.type_slowly(PasswordField, self.user_data["password"])

        self.Random_Time_Delay()

        LoginBtn = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "._6dgzsvq")))

        LoginBtn.click()

        self.Random_Time_Delay()

        FinancialAidBtn.click()"""

        self.Random_Time_Delay()

        total_courses = 9 # Change this to a dynamic function later
        self.Random_Time_Delay()

        course_number = random.randint(1, total_courses)

        CourseSelect = self.locate_element_by_css(f".cui-isChecked > input:nth-child({course_number})")

        CourseSelect.click()
        self.Random_Time_Delay()


        NextButton = self.locate_element_by_css(".css-1guqwvh")
        NextButton.click()
        
        time.sleep(10)
        self.driver.quit()


# Instantiate the bot and execute the login method
bot = CourseraBot()
bot.Course()
