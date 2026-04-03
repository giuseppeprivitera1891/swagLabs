from playwright.async_api import Page

from pages.ProductPage import HomePage
from pages.Login import LoginPage


def test_suite(page:Page):
    page.goto("https://www.saucedemo.com")

    login_page = LoginPage(page)
    login_page.login_to_application("standard_user", "secret_sauce")

    dashboard_page = HomePage(page)
    dashboard_page.add_to_cart()