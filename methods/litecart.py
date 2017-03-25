
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


def check_product_page(wd):
    open_main_page(wd)
    product = wd.find_element_by_css_selector("div#box-campaigns li.product")

    #product name
    mp_product_name = product.find_element_by_css_selector("div.name").text

    #regular price properties obtaining from main page
    regular_price = product.find_element_by_css_selector("s.regular-price")
    main_page_regular_price = regular_price.text
    regular_price_color = regular_price.value_of_css_property("color")
    regular_price_color_RGB = define_RGB_values(regular_price_color)
    regular_price_font_size = regular_price.value_of_css_property("font-size")
    regular_price_font_size_float = define_font_size(regular_price_font_size)
    regular_price_text_decoration = regular_price.value_of_css_property("text-decoration")

    #action price properties obtaining from main page
    action_price = product.find_element_by_css_selector("strong.campaign-price")
    main_page_action_price = action_price.text
    action_price_color = action_price.value_of_css_property("color")
    action_price_color_RGB = define_RGB_values(action_price_color)
    action_price_font_size = action_price.value_of_css_property("font-size")
    action_price_font_size_float = define_font_size(action_price_font_size)
    action_price_font_weight = action_price.value_of_css_property("font-weight")

    #main page properties verification
    regular_price_color_check(regular_price_color_RGB)
    action_price_color_check(action_price_color_RGB)
    assert action_price_font_size_float > regular_price_font_size_float
    assert regular_price_text_decoration == "line-through"
    assert action_price_font_weight == "bold" or action_price_font_weight == "900"

    #open product page
    product.click()
    # product name
    product_name = wd.find_element_by_css_selector("h1.title").text
    # regular price properties obtaining from product page
    product_regular_price = wd.find_element_by_css_selector("s.regular-price")
    product_page_regular_price = product_regular_price.text
    product_regular_price_color = product_regular_price.value_of_css_property("color")
    product_regular_price_color_RGB = define_RGB_values(product_regular_price_color)
    product_regular_price_font_size = product_regular_price.value_of_css_property("font-size")
    product_regular_price_font_size_float = define_font_size(product_regular_price_font_size)
    product_regular_price_text_decoration = product_regular_price.value_of_css_property("text-decoration")
    # action price properties obtaining from product page
    product_action_price = wd.find_element_by_css_selector("strong.campaign-price")
    product_page_action_price = product_action_price.text
    product_action_price_color = product_action_price.value_of_css_property("color")
    product_action_price_color_RGB = define_RGB_values(product_action_price_color)
    product_action_price_font_size = product_action_price.value_of_css_property("font-size")
    product_action_price_font_size_float = define_font_size(product_action_price_font_size)
    product_action_price_font_weight = product_action_price.value_of_css_property("font-weight")

    #compliance verification
    assert mp_product_name == product_name
    assert main_page_regular_price == product_page_regular_price
    assert main_page_action_price == product_page_action_price

    #product page properties verification
    regular_price_color_check(product_regular_price_color_RGB)
    action_price_color_check(product_action_price_color_RGB)
    assert product_action_price_font_size_float > product_regular_price_font_size_float
    assert product_regular_price_text_decoration == "line-through"
    assert product_action_price_font_weight == "bold" or product_action_price_font_weight == "700"


def define_RGB_values(color):
    cleared_color = color[color.find("(")+1:-1]
    color_RGB = [int(color) for color in cleared_color.replace(",", "").split(" ")]
    return color_RGB


def regular_price_color_check(color_RGB):
    assert color_RGB[0] == color_RGB[1] == color_RGB[2]


def action_price_color_check(color_RGB):
    assert color_RGB[1] == 0 and color_RGB[2] == 0


def define_font_size(font_size_string):
    font_size = float(font_size_string[:-2])
    return (font_size)