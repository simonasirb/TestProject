from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Browser:

    BASE_URL = 'http://jules.app/'
    email_selector = (By.CSS_SELECTOR, 'input[placeholder=*Enter your email')

    def __init__(self):
        #self.driver = Chrome(Service(ChromeDriverManager().install()))
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def close(self):
        self.driver.quit()

    def go_to(self, page):
        self.drive.get(f'{self.BASE_URL}{page}')

    def input_email(self, email):
        self.driver.find_element(*self.email_selector).send_keys(email)

    def input_password(self, email):
        password_input = self.driver.find_element(*self.password_selector)


    def input_email(self, email):


