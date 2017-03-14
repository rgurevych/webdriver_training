import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    #wd = webdriver.Firefox()
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://software-testing.ru/")
