import pytest
from selenium import webdriver
from methods import litecart
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def wd(request):
    wd = webdriver.Chrome()
    #wd = webdriver.Ie()
    #wd = webdriver.Firefox(firefox_binary='C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd


def test_check_product_page(wd):
    litecart.open_main_page(wd)
    litecart.check_product_page(wd)
