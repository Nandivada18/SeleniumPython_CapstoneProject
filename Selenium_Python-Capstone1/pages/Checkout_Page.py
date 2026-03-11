import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class CheckoutPage:
    # locators
    Bag = (By.XPATH, "//span[@class='bag bag--float-cart-closed']")
    remove = (By.XPATH, "//div[contains(@class,'shelf-item__del')]")
    Check_btn = (By.XPATH, "//div[@class='buy-btn']")

    def __init__(self, driver):
        self.driver = driver

    # click on Bag and remove item
    def click_Bag(self):
        try:
            self.driver.find_element(*self.Bag).click()
            time.sleep(2)

            self.driver.find_element(*self.remove).click()
            time.sleep(2)

            self.driver.find_element(*self.Check_btn).click()
            time.sleep(3)

        except Exception as e:
            print("Error while performing checkout actions:", e)
            raise

    def checkout(self):
        try:
            self.click_Bag()
        except Exception as e:
            print("Error during checkout process:", e)
            raise