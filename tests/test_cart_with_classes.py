
def test_new_user_registration(app):
    app.main_page.open_main_page()
    app.main_page.add_several_products_to_cart(3)
    app.main_page.open_cart()
    app.cart_page.delete_all_products_from_cart()
