from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common import exceptions as SelEx
from .logger import Logger
from .navigator import Navigator, Page
import time
from enum import StrEnum


class Pets:
    def __init__(self, driver: webdriver.Chrome, logger: Logger):
        self.driver = driver
        self.logger = logger
        self.nav = Navigator(self.driver, self.logger)

    def check_coop(self):
        self.nav.go_to(Page.farm)
        if self.driver.find_elements(By.XPATH, './/a[contains(@href, "coop")]//*[contains(text(),"today")]'):
            return True
        return False

    def check_pasture(self):
        self.nav.go_to(Page.farm)
        if self.driver.find_elements(By.XPATH, './/a[contains(@href, "pasture")]//*[contains(text(),"today")]'):
            return True

    def pet_coop(self):
        self.nav.go_to(Page.coop)
        num = self.driver.find_elements(
                By.XPATH,
                ".//span[contains(@style, 'red')]/parent::*/parent::*/a[contains(@href, 'namechicken.php')]"
            ).__len__()
        if num == 0:
            return
        self.logger.log('pet', f'Number of chickens to pet: {num}', 'Pets')
        while True:
            chicks = self.driver.find_elements(
                By.XPATH,
                ".//span[contains(@style, 'red')]/parent::*/parent::*/a[contains(@href, 'namechicken.php')]"
            )
            if len(chicks) == 0:
                break
            chicks[0].click()
            time.sleep(.5)
            self.driver.find_element(
                By.XPATH,
                ".//div[contains(text(), 'Pet Chicken')]/./parent::div/parent::div/parent::a"
            ).click()
            time.sleep(.5)
            self.driver.find_element(By.XPATH, ".//span[text()='OK']").click()
            time.sleep(.5)
        self.logger.log('pet', 'Finished petting chickens', 'Pets')


