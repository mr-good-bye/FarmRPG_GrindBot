from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common import exceptions as SelEx
from .logger import Logger
import time
from enum import StrEnum


class Page(StrEnum):
    index = 'https://farmrpg.com/index.php'
    farm = 'farm'
    coop = 'coop'


class Navigator:
    def __init__(self, driver: webdriver.Chrome, logger: Logger):
        self.driver = driver
        self.logger = logger

    def go_to(self, page: Page):
        if page.value.startswith('http'):
            self.driver.get(page.value)
        elif page.value == 'coop':
            self._coop()
        elif page.value == 'farm':
            self._farm()
        self.logger.log('debug', f'Navigated to {page.name}', 'Navigator')

    def _coop(self):
        self.go_to(Page.farm)
        time.sleep(.5+.3)
        self.driver.find_element(By.XPATH, ".//a[contains(@href, 'coop')]").click()
        time.sleep(.5+.3)

    def _farm(self):
        self.go_to(Page.index)
        time.sleep(.5)
        self.driver.find_element(By.XPATH, ".//a[contains(@href, 'xfarm.php')]").click()
        time.sleep(.5)

