import pytest
from selenium import webdriver


@pytest.fixture
def wd(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(wd):
    wd.get("http://localhost/litecart/admin/")
    wd.find_element_by_name("username").send_keys("admin")
    wd.find_element_by_name("password").send_keys("admin")
    wd.find_element_by_name("login").click()
    assert not wd.current_url.endswith("/login_page.php")