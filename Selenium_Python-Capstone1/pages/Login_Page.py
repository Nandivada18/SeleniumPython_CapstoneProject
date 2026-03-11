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
        try:
            self.driver.find_element(*self.Sign_btn).click()
            time.sleep(2)
        except Exception as e:
            print("Error while clicking Sign In:", e)
            raise

    def user(self, Username, Password):
        try:
            self.driver.find_element(*self.Username).click()
            time.sleep(1)
            user_option = (By.XPATH, f"//div[text()='{Username}']")
            self.driver.find_element(*user_option).click()
            time.sleep(2)

            self.driver.find_element(*self.Password).click()
            time.sleep(1)

            pass_option = (By.XPATH, f"//div[text()='{Password}']")
            self.driver.find_element(*pass_option).click()
            time.sleep(2)

        except Exception as e:
            print("Error while selecting username or password:", e)
            raise

    def click_login(self):
        try:
            self.driver.find_element(*self.Login_btn).click()
            time.sleep(3)
        except Exception as e:
            print("Error while clicking Login button:", e)
            raise

    def login(self, Username, Password):
        try:
            self.click_signin()
            self.user(Username, Password)
            self.click_login()
        except Exception as e:
            print("Error during login process:", e)
            raise

    def get_error_message(self):
        try:
            return self.driver.find_element(*self.error_msg).text
        except Exception as e:
            print("Error getting error message:", e)
            raise