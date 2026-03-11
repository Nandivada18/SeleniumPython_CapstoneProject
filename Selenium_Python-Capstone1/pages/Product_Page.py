import time
from selenium.webdriver.common.by import By

class ProductPage:
    # locators
    search = (By.XPATH, "//input[@placeholder='Search']")
    search_btn = (By.XPATH, "//button[@role='button']")
    product1 = (By.XPATH, "(//div[text()='Add to cart'])[1]")
    samsung = (By.XPATH, "//span[normalize-space()='Samsung']")
    product2 = (By.XPATH, "(//div[text()='Add to cart'])[2]")
    Google = (By.XPATH, "//span[normalize-space()='Google']")
    product3 = (By.XPATH, "(//div[text()='Add to cart'])[3]")
    cross = (By.XPATH, "//div[@class='float-cart__close-btn']")

    def __init__(self, driver):
        self.driver = driver

    # Search for product
    def enter_search(self, Product_Name):
        try:
            self.driver.find_element(*self.search).send_keys(Product_Name)
            time.sleep(2)
            self.driver.find_element(*self.search_btn).click()
            time.sleep(2)
        except Exception as e:
            print("Error while searching product:", e)
            raise

    # click on add to cart button
    def click_add(self):
        try:
            self.driver.find_element(*self.product1).click()
            time.sleep(2)

            self.driver.find_element(*self.samsung).click()
            time.sleep(2)

            self.driver.find_element(*self.product2).click()
            time.sleep(2)

            self.driver.find_element(*self.samsung).click()
            time.sleep(2)

            self.driver.find_element(*self.Google).click()
            time.sleep(2)

            self.driver.find_element(*self.product3).click()
            time.sleep(2)

            self.driver.find_element(*self.cross).click()
            time.sleep(3)

        except Exception as e:
            print("Error while adding products to cart:", e)
            raise

    def product(self, Product_Name):
        try:
            self.enter_search(Product_Name)
            self.click_add()
        except Exception as e:
            print("Error in product selection process:", e)
            raise