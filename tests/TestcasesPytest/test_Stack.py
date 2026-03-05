import pytest
from pages.Login_Page import LoginPage
from pages.Product_Page import ProductPage
from pages.Checkout_Page import CheckoutPage
from pages.Shipping_Page import ShippingPage
from pages.Receipt_Page import ReceiptPage
from pages.Logout_Page import LogoutPage
from utilities.logger import get_logger
from utilities.excel_utils import get_excel_data

logger = get_logger()

test_data = get_excel_data("C://Users//prasa//PycharmProjects//Selenium_Python-Capstone1//testdata//login_data.xlsx","Sheet2")

class TestLogin:

    @pytest.mark.parametrize("Username, Password, Product_Name, First_Name, Last_Name, Address, State, Postal_code",test_data)
    def test_excel(self, driver, Username, Password, Product_Name, First_Name, Last_Name, Address, State, Postal_code):

        logger.info("Opening application")

        # Login Page
        login = LoginPage(driver)
        login.login(Username, Password)
        logger.info("Successfully Logged in")

        if Password == "testingisfun99":
            assert "StackDemo" in driver.title
        else:
            assert "Invalid credentials" in login.get_error_message()

        logger.info("Now adding Products")
        # Product Page
        product = ProductPage(driver)
        product.product(Product_Name)
        logger.info("Products added to cart")

        logger.info("Checkout the Products")
        # Checkout Page
        check = CheckoutPage(driver)
        check.checkout()

        logger.info("Now Giving Shipping Address")
        # Shipping Page
        ship = ShippingPage(driver)
        ship.ship_address(First_Name, Last_Name, Address, State, Postal_code)

        assert "Your Order has been successfully placed." in driver.page_source

        logger.info("Successfully Ordered Placed")
        # Receipt Page
        receipt = ReceiptPage(driver)
        receipt.receipt_page()
        logger.info("Receipt Successfully Downloaded")

        logger.info("Back to Home Page")
        # Logout Page
        logout = LogoutPage(driver)
        logout.click_Logout()
        logger.info("Logged out Successfully")




