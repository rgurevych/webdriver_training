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
    litecart.login_to_admin(wd)
    name = generators.generate_product_name()
    litecart.add_new_product(wd, name)
    litecart.verify_product_presence(wd, name)
    litecart.logout_from_admin(wd)

