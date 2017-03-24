import pytest
from selenium import webdriver
from methods import litecart


@pytest.fixture
def wd(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_countries_abc(wd):
    litecart.login_to_admin(wd)
    litecart.check_countries_abc(wd)
    litecart.logout_from_admin(wd)


def test_zones_abc(wd):
    litecart.login_to_admin(wd)
    litecart.check_zones_abc(wd)
    litecart.logout_from_admin(wd)