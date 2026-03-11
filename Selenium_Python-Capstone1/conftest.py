# create a fixture for Invoke chrome browser and close the browser

import pytest
from datetime import datetime
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="function")
def driver(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://bstackdemo.com/")

    request.cls.driver = driver
    yield driver
    driver.quit()


# screenshot taking if the test case fails
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            file_name = f"{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            file_path = os.path.join(screenshots_dir, file_name)
            driver.save_screenshot(file_path)

