import json

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


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


def add_product_and_open_checkout(page):

    # Login
    login_to_application(page)

    # Product page
    product_page = ProductPage(page)

    product_page.add_product_to_cart(
        TEST_DATA["products"]["backpack"]
    )

    # Make sure product was added
    assert product_page.get_cart_count() == 1

    # Open cart
    product_page.open_cart()

    # Make sure cart page loaded
    page.wait_for_url(
        "**/cart.html",
        timeout=15000
    )

    # Open checkout
    cart_page = CartPage(page)

    cart_page.proceed_to_checkout()

    # Make sure checkout information page loaded
    page.wait_for_url(
        "**/checkout-step-one.html",
        timeout=15000
    )

    # Make sure the actual checkout form is visible
    page.locator(
        "[data-test='firstName']"
    ).wait_for(
        state="visible",
        timeout=15000
    )


def test_checkout_page_opens(page):

    add_product_and_open_checkout(page)

    checkout_page = CheckoutPage(page)

    assert page.url.endswith(
        "/checkout-step-one.html"
    )

    assert checkout_page.get_checkout_title() == (
        "Checkout: Your Information"
    )


def test_enter_customer_details(page):

    add_product_and_open_checkout(page)

    checkout_page = CheckoutPage(page)

    checkout_page.enter_customer_details(
        TEST_DATA["customer"]["first_name"],
        TEST_DATA["customer"]["last_name"],
        TEST_DATA["customer"]["postal_code"]
    )

    checkout_page.continue_to_overview()

    assert page.url.endswith(
        "/checkout-step-two.html"
    )

    assert checkout_page.get_checkout_title() == (
        "Checkout: Overview"
    )


def test_complete_checkout(page):

    add_product_and_open_checkout(page)

    checkout_page = CheckoutPage(page)

    checkout_page.enter_customer_details(
        TEST_DATA["customer"]["first_name"],
        TEST_DATA["customer"]["last_name"],
        TEST_DATA["customer"]["postal_code"]
    )

    checkout_page.continue_to_overview()

    assert page.url.endswith(
        "/checkout-step-two.html"
    )

    assert checkout_page.get_checkout_title() == (
        "Checkout: Overview"
    )

    checkout_page.finish_checkout()

    assert page.url.endswith(
        "/checkout-complete.html"
    )

    assert checkout_page.get_confirmation_message() == (
        "Thank you for your order!"
    )