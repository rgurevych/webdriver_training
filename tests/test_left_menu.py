import pytest
from selenium import webdriver
from methods import litecart


@pytest.fixture
def wd(request):
    wd = webdriver.Chrome()
    #wd.implicitly_wait(1)
    #wd = webdriver.Firefox(capabilities={"marionette": True}, firefox_binary ='C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')
    request.addfinalizer(wd.quit)
    return wd


def test_left_menu_headers_presence(wd):
    litecart.login_to_admin(wd)
    litecart.check_left_menu_elements(wd)
    litecart.logout_from_admin(wd)