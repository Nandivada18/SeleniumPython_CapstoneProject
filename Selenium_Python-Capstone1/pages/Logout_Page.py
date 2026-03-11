import time
from selenium.webdriver.common.by import By

class LogoutPage:
    # locators
    logout_btn = (By.XPATH, "//span[@id='signin']")

    def __init__(self, driver):
        self.driver = driver

    # click on Logout
    def click_Logout(self):
        try:
            self.driver.find_element(*self.logout_btn).click()
            time.sleep(3)
        except Exception as e:
            print("Error while clicking logout:", e)
            raise

    def Logout(self):
        try:
            self.click_Logout()
        except Exception as e:
            print("Error during logout process:", e)
            raise