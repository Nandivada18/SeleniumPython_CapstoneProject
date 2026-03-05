from selenium.webdriver.common.by import By
import time

class LoginPage:
    Sign_btn = (By.XPATH, "//span[@id='signin']")
    Username = (By.XPATH, "//div[contains(text(),'Select Username')]")
    Password = (By.XPATH, "//div[contains(text(),'Select Password')]")
    Login_btn = (By.XPATH, "//button[@id='login-btn']")
    error_msg = (By.XPATH, "//h3[@class='api-error']")
    def __init__(self, driver):
        self.driver = driver

    def click_signin(self):
        self.driver.find_element(*self.Sign_btn).click()
        time.sleep(2)

    def user(self,Username,Password):
        self.driver.find_element(*self.Username).click()
        user_option = (By.XPATH, f"//div[text()='{Username}']")
        self.driver.find_element(*user_option).click()
        time.sleep(2)
        self.driver.find_element(*self.Password).click()
        time.sleep(2)
        pass_option = (By.XPATH, f"//div[text()='{Password}']")
        self.driver.find_element(*pass_option).click()
        time.sleep(2)

    def click_login(self):
        self.driver.find_element(*self.Login_btn).click()
        time.sleep(2)

    def login(self,Username,Password):
        self.click_signin()
        self.user(Username,Password)
        self.click_login()

    def get_error_message(self):
        return self.driver.find_element(*self.error_msg).text
