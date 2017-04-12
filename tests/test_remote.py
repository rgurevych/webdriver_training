from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_cap = {'browser': 'chrome', 'build': 'First build', 'browserstack.debug': 'true' }

driver = webdriver.Remote(
    command_executor='http://rostyslavgurevyc1:3CLVHGxSouCuMipSCkzn@hub.browserstack.com:80/wd/hub',
    desired_capabilities=desired_cap)

driver.get("http://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
elem = driver.find_element_by_name("q")
elem.send_keys("BrowserStack")
elem.submit()

driver.quit()