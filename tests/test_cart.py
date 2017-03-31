import pytest
from selenium import webdriver
from methods import litecart, generators


@pytest.fixture
def wd(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_new_user_registration(wd):
    litecart.open_main_page(wd)
    for i in range (1, 4):
        litecart.add_product_to_cart(wd, i)
        litecart.open_main_page(wd)
    litecart.open_cart(wd)
    litecart.delete_all_products_from_cart(wd)
