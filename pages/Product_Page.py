import time
from selenium.webdriver.common.by import By

class ProductPage:
    # locators
    search = (By.XPATH, "//input[@placeholder='Search']")
    search_btn = (By.XPATH, "//button[@role='button']")
    product1 = (By.XPATH, "//div[@id='1']//div[@class='shelf-item__buy-btn'][normalize-space()='Add to cart']")
    samsung = (By.XPATH, "//span[normalize-space()='Samsung']")
    product2 = (By.XPATH, "//div[@id='11']//div[@class='shelf-item__buy-btn'][normalize-space()='Add to cart']")
    Google = (By.XPATH, "//span[normalize-space()='Google']")
    product3 = (By.XPATH, "//div[@id='17']//div[@class='shelf-item__buy-btn'][normalize-space()='Add to cart']")
    cross = (By.XPATH, "//div[@class='float-cart__close-btn']")

    def __init__(self, driver):
        self.driver = driver

    # Search for product
    def enter_search(self,Product_Name):
        self.driver.find_element(*self.search).send_keys(Product_Name)
        time.sleep(2)
        self.driver.find_element(*self.search_btn).click()
        time.sleep(2)

    # click on add to cart button
    def click_add(self):
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
        time.sleep(1)

    def product(self,Product_Name):
        self.enter_search(Product_Name)
        self.click_add()
