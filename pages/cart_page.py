from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, app):
        self.app = app
        self.wd = app.wd
        self.wait = app.wait

    def delete_all_products_from_cart(self):
        while (len(self.wd.find_elements_by_css_selector("table.dataTable td.item")) > 0):
            if len(self.wd.find_elements_by_css_selector("ul.shortcuts a")) > 0:
                self.wd.find_element_by_css_selector("ul.shortcuts a").click()
            table_line = self.wd.find_element_by_css_selector("table.dataTable td.item")
            self.wd.find_element_by_name("remove_cart_item").click()
            self.wait.until(EC.staleness_of(table_line))