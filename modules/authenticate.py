from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common import exceptions as SelEx
from .logger import Logger
import time


class Authenticator:
    def __init__(self, login, password, driver: webdriver.Chrome, logger: Logger):
        self.login = login
        self.password = password
        self.driver = driver
        self.logger = logger

    def __call__(self):
        self.driver.get('https://farmrpg.com/index.php#!/login.php')

        username_box = self.driver.find_element(By.NAME, "username")
        username_box.clear()
        username_box.send_keys(self.login)

        pwd_box = self.driver.find_element(By.NAME, "password")
        pwd_box.clear()
        pwd_box.send_keys(self.password)

        pwd_box.send_keys(Keys.RETURN)

        time.sleep(.5+.7)

        if len(self.driver.find_elements(By.XPATH, './/a[@href="logout.php"]')) == 0:
            raise ValueError('Login failed. Check credentials at config.py')
        else:
            self.logger.log('info', 'Logged in', 'Authenticator')

    def logout(self):
        self.driver.find_element(By.XPATH, './/a[@href="logout.php"]').click()
        self.logger.log('info', 'Logged out', 'Authenticator')

