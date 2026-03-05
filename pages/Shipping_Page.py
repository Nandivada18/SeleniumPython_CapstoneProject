import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ShippingPage:
    # locators
    first_name = (By.XPATH, "//input[@id='firstNameInput']")
    last_name = (By.XPATH, "//input[@id='lastNameInput']")
    address = (By.XPATH, "//input[@id='addressLine1Input']")
    state = (By.XPATH, "//input[@id='provinceInput']")
    postal_code = (By.XPATH, "//input[@id='postCodeInput']")
    Submit_btn = (By.XPATH, "//button[@id='checkout-shipping-continue']")
    def __init__(self, driver):
        self.driver = driver

    # click on Bag and remove item
    def Ship_add(self,First_Name,Last_Name,Address,State,Postal_code):
        self.driver.find_element(*self.first_name).send_keys(First_Name)
        time.sleep(1)
        self.driver.find_element(*self.last_name).send_keys(Last_Name)
        time.sleep(1)
        self.driver.find_element(*self.address).send_keys(Address)
        time.sleep(1)
        self.driver.find_element(*self.state).send_keys(State)
        time.sleep(1)
        self.driver.find_element(*self.postal_code).send_keys(Postal_code)
        time.sleep(1)
        self.driver.find_element(*self.Submit_btn).click()
        time.sleep(2)

    def ship_address(self,First_Name,Last_Name,Address,State,Postal_code):
        self.Ship_add(First_Name,Last_Name,Address,State,Postal_code)