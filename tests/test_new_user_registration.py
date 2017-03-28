import pytest
from selenium import webdriver
from methods import litecart, generators


@pytest.fixture
def wd(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd


def test_new_user_registration(wd):
    litecart.open_main_page(wd)
    email = generators.generate_email()
    litecart.new_user_registration(wd, email)
    litecart.user_logout(wd)
    litecart.user_login(wd, email)
    litecart.user_logout(wd)
