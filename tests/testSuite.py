from playwright.async_api import Page

from pages.Login import LoginPage


def test_suite(page:Page):
    page.goto("https://www.saucedemo.com")

    login_page = LoginPage(page)
    login_page.login_to_application("standard_user", "secret_sauce")