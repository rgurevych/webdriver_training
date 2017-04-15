from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ProductPage:

    def __init__(self, app):
        self.app = app
        self.wd = app.wd
        self.wait = app.wait

    def add_product_to_cart(self, number):
        if len(self.wd.find_elements_by_name("options[Size]")) > 0:
            select_size = Select(self.wd.find_element_by_name("options[Size]"))
            select_size.select_by_visible_text("Small")
        self.wd.find_element_by_name("add_cart_product").click()
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.quantity"), str(number)))
