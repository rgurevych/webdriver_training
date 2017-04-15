from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wait = WebDriverWait(self.wd, 10)
        self.main_page = MainPage(self)
        self.product_page = ProductPage(self)
        self.cart_page = CartPage(self)

    def quit(self):
        self.wd.quit()
