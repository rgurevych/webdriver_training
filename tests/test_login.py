import pytest
from selenium import webdriver
from methods import litecart
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


@pytest.fixture
def wd(request):
    wd = webdriver.Chrome()
    #wd = webdriver.Firefox(capabilities={"marionette": True}, firefox_binary ='C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')
    #print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_login(wd):
    litecart.login_to_admin(wd)




