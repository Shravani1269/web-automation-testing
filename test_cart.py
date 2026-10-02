from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


def login_to_application(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert login_page.is_login_successful()


def add_product_and_open_cart(page):
    login_to_application(page)

    product_page = ProductPage(page)

    product_page.add_product_to_cart("Sauce Labs Backpack")
    product_page.open_cart()


def test_cart_contains_added_product(page):
    add_product_and_open_cart(page)

    cart_page = CartPage(page)

    assert cart_page.get_item_count() == 1
    assert "Sauce Labs Backpack" in cart_page.get_item_names()


def test_cart_product_price(page):
    add_product_and_open_cart(page)

    cart_page = CartPage(page)

    prices = cart_page.get_item_prices()

    assert len(prices) == 1
    assert prices[0] > 0


def test_multiple_products_in_cart(page):
    login_to_application(page)

    product_page = ProductPage(page)

    product_page.add_product_to_cart("Sauce Labs Backpack")
    product_page.add_product_to_cart("Sauce Labs Bike Light")
    product_page.open_cart()

    cart_page = CartPage(page)

    names = cart_page.get_item_names()

    assert len(names) == 2
    assert "Sauce Labs Backpack" in names
    assert "Sauce Labs Bike Light" in names


def test_remove_product_from_cart(page):
    add_product_and_open_cart(page)

    cart_page = CartPage(page)

    cart_page.remove_product("Sauce Labs Backpack")

    assert cart_page.get_item_count() == 0


def test_continue_shopping(page):
    add_product_and_open_cart(page)

    cart_page = CartPage(page)

    cart_page.continue_shopping()

    assert "/inventory.html" in page.url