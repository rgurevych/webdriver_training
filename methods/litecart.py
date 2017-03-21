
def login_to_admin(wd):
    wd.get("http://localhost/litecart/admin/")
    wd.find_element_by_name("username").send_keys("admin")
    wd.find_element_by_name("password").send_keys("admin")
    wd.find_element_by_name("login").click()
    assert not wd.current_url.endswith("/login.php")


def logout_from_admin(wd):
    wd.find_element_by_css_selector("i.fa.fa-sign-out").click()
    assert wd.current_url.endswith("/login.php")


def check_left_menu_elements(wd):
    menu_list = wd.find_elements_by_css_selector("li#app-")
    for i in range(0, len(menu_list)):
        wd.find_elements_by_css_selector("li#app-")[i].click()
        assert len(wd.find_elements_by_css_selector("td#content h1")) == 1
        submenu_list = wd.find_elements_by_css_selector("li#app-")[i].find_elements_by_css_selector("li")
        if len(submenu_list)>0:
            check_left_sumbenu_elements(wd, i, len(submenu_list))


def check_left_sumbenu_elements(wd, i, submenu_length):
    for j in range(0, submenu_length):
        wd.find_elements_by_css_selector("li#app-")[i].find_elements_by_css_selector("li")[j].click()
        assert len(wd.find_elements_by_css_selector("td#content h1")) == 1


def open_main_page(wd):
    wd.get("http://localhost/litecart/")


def check_stickers_presence(wd):
    products_list = wd.find_elements_by_css_selector("li.product")
    for product in products_list:
        assert len(product.find_elements_by_css_selector("div[class ^= sticker]")) == 1
