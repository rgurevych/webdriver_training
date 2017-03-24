import time

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


def check_countries_abc(wd):
    wd.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    country_list = wd.find_elements_by_css_selector("tr.row")
    countries = []
    countries_with_several_zones = []
    for row in country_list:
        countries.append(row.find_element_by_css_selector("a").text)
        if row.find_elements_by_css_selector("td")[5].text != "0":
            countries_with_several_zones.append(country_list.index(row))
    assert countries == sorted(countries)
    check_zones_abc_in_country(wd, countries_with_several_zones)


def check_zones_abc_in_country(wd, countries_with_several_zones):
    for country_list_number in countries_with_several_zones:
        wd.get("http://localhost/litecart/admin/?app=countries&doc=countries")
        country = wd.find_elements_by_css_selector("tr.row")[country_list_number]
        country.find_element_by_css_selector("a").click()
        zones_list = wd.find_elements_by_css_selector("table#table-zones tr")
        zones_list.pop(0)
        zones_list.pop()
        zones = []
        for row in zones_list:
            zones.append(row.find_elements_by_css_selector("td")[2].text)
        assert zones == sorted(zones)


def check_zones_abc(wd):
    wd.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    zones_list = wd.find_elements_by_css_selector("tr.row")
    for i in range(0, len(zones_list)):
        wd.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
        wd.find_elements_by_css_selector("tr.row")[i].find_element_by_css_selector("a").click()
        zones_list = wd.find_elements_by_css_selector("table#table-zones tr")
        zones_list.pop(0)
        zones_list.pop()
        zones = []
        country_in_header = wd.find_element_by_css_selector("input[name=name]").get_attribute("value")
        for row in zones_list:
            country_in_list = row.find_elements_by_css_selector("td")[1].find_element_by_css_selector("span.selection").text
            #This part defines whether the list describes zones in country or countries in area (such as European Union)
            if country_in_list in country_in_header:
                zone_name = row.find_elements_by_css_selector("td")[2].find_element_by_css_selector("option[selected = selected]").text
                zones.append(zone_name)
            else:
                zones.append(country_in_list)
        assert zones == sorted(zones)
