import pytest
from selenium import webdriver
from methods import litecart


@pytest.fixture
def wd(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_log_messages(wd):
    litecart.login_to_admin(wd)
    litecart.open_products_links_and_check_log(wd)
    litecart.logout_from_admin(wd)
