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
        print("Petting chickens")
        pets.pet_coop()
    if pets.check_pasture():
        print("Petting cows")
        pets.pet_pasture()
    auth.logout()
