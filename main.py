import modules
from selenium.webdriver import Chrome
from config import Config


if __name__ == '__main__':
    logger = modules.Logger('LaRos')
    driver = Chrome()
    auth = modules.Authenticator(Config.login, Config.password, driver, logger)
    pets = modules.Pets(driver, logger)
    auth()
    if pets.check_coop():
        print("Petting")
        pets.pet_coop()
    auth.logout()
