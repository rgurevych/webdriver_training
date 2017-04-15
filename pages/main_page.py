
class MainPage:

    def __init__(self, app):
        self.app = app
        self.wd = app.wd
        self.wait = app.wait

    def open_main_page(self):
        self.wd.get("http://localhost/litecart/")
        return self

    def add_several_products_to_cart(self, amount):
        for i in range(1, amount+1):
            self.select_first_product()
            self.app.product_page.add_product_to_cart(i)
            self.open_main_page()

    def select_first_product(self):
        self.wd.find_element_by_css_selector("li.product").click()

    def open_cart(self):
        self.wd.find_element_by_partial_link_text("Checkout").click()



