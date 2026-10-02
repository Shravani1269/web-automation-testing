import json
import pytest

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


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


def add_product_and_open_cart(page):

    login_to_application(page)

    product_page = ProductPage(page)

    product_page.add_product_to_cart(
        TEST_DATA["products"]["backpack"]
    )

    product_page.open_cart()


@pytest.mark.smoke
@pytest.mark.regression
def test_cart_contains_added_product(page):

    add_product_and_open_cart(page)

    cart_page = CartPage(page)

    assert cart_page.get_item_count() == 1

    assert (
        TEST_DATA["products"]["backpack"]
        in cart_page.get_item_names()
    )


@pytest.mark.regression
def test_cart_product_price(page):

    add_product_and_open_cart(page)

    cart_page = CartPage(page)

    prices = cart_page.get_item_prices()

    assert len(prices) == 1
    assert prices[0] > 0


@pytest.mark.regression
def test_multiple_products_in_cart(page):

    login_to_application(page)

    product_page = ProductPage(page)

    product_page.add_product_to_cart(
        TEST_DATA["products"]["backpack"]
    )

    product_page.add_product_to_cart(
        TEST_DATA["products"]["bike_light"]
    )

    product_page.open_cart()

    cart_page = CartPage(page)

    names = cart_page.get_item_names()

    assert len(names) == 2

    assert TEST_DATA["products"]["backpack"] in names

    assert TEST_DATA["products"]["bike_light"] in names


@pytest.mark.regression
def test_remove_product_from_cart(page):

    add_product_and_open_cart(page)

    cart_page = CartPage(page)

    cart_page.remove_product(
        TEST_DATA["products"]["backpack"]
    )

    assert cart_page.get_item_count() == 0


@pytest.mark.regression
def test_continue_shopping(page):

    add_product_and_open_cart(page)

    cart_page = CartPage(page)

    cart_page.continue_shopping()

    assert "/inventory.html" in page.url