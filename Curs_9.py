import unittest

from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Test(unittest.TestCase):
    base_url = 'https://www.itfactory.ro/ta-29/'
    password_for_29 = '7eD8edeERteMczy'

    def test_open_the_IFpage_for_29(self):
        driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
        driver.get(self.base_url)
        driver.maximize_window()
        # sleep(5)
        # driver.implicitly_wait(1)
        # element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
        password_input = driver.find_element(By.CSS_SELECTOR, "#pwbox-16369")

        password_input.send_keys(self.password_for_29)

        submit_button = driver.find_element(By.CSS_SELECTOR, 'input[name="Submit"')
        submit_button.click()

        actual_url = driver.current_url
        trainer_name = driver.find_element(By.CSS_SELECTOR, '.elementor-text-editor > ul > li:nth-child(2) > strong')

        assert actual_url == 'https://www.itfactory.ro/ta-29/', 'You are not on the correct page!'
        assert trainer_name.text.contains('Mihai Vaman')
        driver.delete_all_cookies()
        driver.quit()

    def test_check_courses_for_29(self):
        driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
        driver.get(self.base_url)
        driver.maximize_window()

        password_input = driver.find_element(By.CSS_SELECTOR, '#pwbox-16369')
        password_input.send_keys(self.password_for_29)

        submit_button = driver.find_element(By.CSS_SELECTOR, 'input[name="Submit"')
        submit_button.click()

        ActionChains(driver).move_to_element(
            driver.find_element(By.CSS_SELECTOR, '.elementor-element-7f375f3c')).perform()

        curses_list = driver.find_elements(By.CSS_SELECTOR, '.elementor-element-16a244fe h2')
        print('\n')
        for curse in curses_list:
            print(curse.text)

        assert len(curses_list) == 4
        driver.delete_all_cookies()
        driver.quit()