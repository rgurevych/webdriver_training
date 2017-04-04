import pytest
from selenium import webdriver
from methods import litecart


@pytest.fixture
def wd(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_links(wd):
    litecart.login_to_admin(wd)
    litecart.check_links_on_country_page(wd)
    litecart.logout_from_admin(wd)
