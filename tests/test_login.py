import pytest

from pages.login_page import LoginPage


@pytest.mark.smoke
@pytest.mark.regression
def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert login_page.is_login_successful()


@pytest.mark.regression
def test_invalid_password(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "wrong_password")

    assert "Username and password do not match any user in this service" in \
           login_page.get_error_message()


@pytest.mark.regression
def test_invalid_username(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("invalid_user", "secret_sauce")

    assert "Username and password do not match any user in this service" in \
           login_page.get_error_message()


@pytest.mark.regression
def test_empty_username(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("", "secret_sauce")

    assert "Username is required" in login_page.get_error_message()


@pytest.mark.regression
def test_empty_password(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "")

    assert "Password is required" in login_page.get_error_message()


@pytest.mark.regression
def test_locked_out_user(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    assert "Sorry, this user has been locked out" in \
           login_page.get_error_message()