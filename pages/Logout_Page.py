import time
from selenium.webdriver.common.by import By

class LogoutPage:
    # locators
    logout_btn = (By.XPATH, "//span[@id='signin']")

    def __init__(self, driver):
        self.driver = driver

    # click on Logout
    def click_Logout(self):
        self.driver.find_element(*self.logout_btn).click()
        time.sleep(2)

    def Logout(self):
        self.click_Logout()