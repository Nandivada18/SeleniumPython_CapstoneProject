import time
from selenium.webdriver.common.by import By
import os.path

DOWNLOAD_DIR = "C://Users//prasa//Downloads"

class ReceiptPage:
    # locators
    download_btn = (By.XPATH, "//a[@id='downloadpdf']")
    contin_btn = (By.XPATH, "//button[@class='button button--tertiary optimizedCheckout-buttonSecondary']")

    def __init__(self, driver):
        self.driver = driver

    # download receipt
    def click_down(self):
        try:
            self.driver.find_element(*self.download_btn).click()
            time.sleep(2)

            file_path = os.path.join(DOWNLOAD_DIR, "confirmation.pdf")
            assert os.path.exists(file_path)
            time.sleep(2)

        except Exception as e:
            print("Error while downloading receipt:", e)
            raise

    def click_continue(self):
        try:
            self.driver.find_element(*self.contin_btn).click()
            time.sleep(3)
        except Exception as e:
            print("Error while clicking continue button:", e)
            raise

    def receipt_page(self):
        try:
            self.click_down()
            self.click_continue()
        except Exception as e:
            print("Error in receipt page process:", e)
            raise