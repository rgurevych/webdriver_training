import pytest
from selenium import webdriver
from methods import litecart


@pytest.fixture
def wd(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_stickers_presence(wd):
    litecart.open_main_page(wd)
    litecart.check_stickers_presence(wd)
