import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture
def driver(request):
    #wd = webdriver.Firefox()
    #wd = webdriver.Chrome()
    wd = webdriver.Remote(command_executor='http://rostyslavgurevyc1:3CLVHGxSouCuMipSCkzn@hub.browserstack.com:80/wd/hub',
        desired_capabilities={'browser': 'chrome', 'build': 'First build', 'browserstack.debug': 'true' })
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://software-testing.ru/")
    time.sleep(15)