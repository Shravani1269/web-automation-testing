import json
import pytest

from pages.login_page import LoginPage
from pages.product_page import ProductPage


# Load test data
with open("test_data/test_data.json", "r") as file:
    TEST_DATA = json.load(file)


def login_to_application(page):
    login_page = LoginPage(page)

    login_page.open()

    login_page.login(
        TEST_DATA["login"]["valid_username"],
        TEST_DATA["login"]["valid_password"]
    )

    assert login_page.is_login_successful()


@pytest.mark.smoke
@pytest.mark.regression
def test_products_are_displayed(page):
    login_to_application(page)

    product_page = ProductPage(page)

    assert product_page.get_product_count() == 6


@pytest.mark.regression
def test_product_names_are_displayed(page):
    login_to_application(page)

    product_page = ProductPage(page)

    names = product_page.get_product_names()

    assert len(names) == 6
    assert TEST_DATA["products"]["backpack"] in names


@pytest.mark.regression
def test_product_prices_are_displayed(page):
    login_to_application(page)

    product_page = ProductPage(page)

    prices = product_page.get_product_prices()

    assert len(prices) == 6
    assert all(price > 0 for price in prices)


@pytest.mark.regression
def test_sort_products_low_to_high(page):
    login_to_application(page)

    product_page = ProductPage(page)

    product_page.sort_products("lohi")

    prices = product_page.get_product_prices()

    assert prices == sorted(prices)


@pytest.mark.regression
def test_sort_products_high_to_low(page):
    login_to_application(page)

    product_page = ProductPage(page)

    product_page.sort_products("hilo")

    prices = product_page.get_product_prices()

    assert prices == sorted(prices, reverse=True)


@pytest.mark.smoke
@pytest.mark.regression
def test_add_product_to_cart(page):
    login_to_application(page)

    product_page = ProductPage(page)

    product_page.add_product_to_cart(
        TEST_DATA["products"]["backpack"]
    )

    assert product_page.get_cart_count() == 1


@pytest.mark.regression
def test_add_multiple_products_to_cart(page):
    login_to_application(page)

    product_page = ProductPage(page)

    product_page.add_product_to_cart(
        TEST_DATA["products"]["backpack"]
    )

    product_page.add_product_to_cart(
        TEST_DATA["products"]["bike_light"]
    )

    assert product_page.get_cart_count() == 2