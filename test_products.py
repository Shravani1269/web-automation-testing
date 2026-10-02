from pages.login_page import LoginPage
from pages.product_page import ProductPage


def login_to_application(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert login_page.is_login_successful()


def test_products_are_displayed(page):
    login_to_application(page)

    product_page = ProductPage(page)

    assert product_page.get_product_count() == 6


def test_product_names_are_displayed(page):
    login_to_application(page)

    product_page = ProductPage(page)

    names = product_page.get_product_names()

    assert len(names) == 6
    assert "Sauce Labs Backpack" in names


def test_product_prices_are_displayed(page):
    login_to_application(page)

    product_page = ProductPage(page)

    prices = product_page.get_product_prices()

    assert len(prices) == 6
    assert all(price > 0 for price in prices)


def test_sort_products_low_to_high(page):
    login_to_application(page)

    product_page = ProductPage(page)

    product_page.sort_products("lohi")

    prices = product_page.get_product_prices()

    assert prices == sorted(prices)


def test_sort_products_high_to_low(page):
    login_to_application(page)

    product_page = ProductPage(page)

    product_page.sort_products("hilo")

    prices = product_page.get_product_prices()

    assert prices == sorted(prices, reverse=True)


def test_add_product_to_cart(page):
    login_to_application(page)

    product_page = ProductPage(page)

    product_page.add_product_to_cart("Sauce Labs Backpack")

    assert product_page.get_cart_count() == 1


def test_add_multiple_products_to_cart(page):
    login_to_application(page)

    product_page = ProductPage(page)

    product_page.add_product_to_cart("Sauce Labs Backpack")
    product_page.add_product_to_cart("Sauce Labs Bike Light")

    assert product_page.get_cart_count() == 2