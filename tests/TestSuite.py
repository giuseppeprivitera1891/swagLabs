from playwright.async_api import Page

from pages.CartPage import CartPage
from pages.CheckoutInformationPage import CheckoutInformationPage
from pages.CheckoutOverviewPage import CheckoutOverviewPage
from pages.LoginPage import LoginPage
from pages.ProductPage import ProductPage


def test_suite(page:Page):
    page.goto("https://www.saucedemo.com")

    login_page = LoginPage(page)
    login_page.login_to_application("standard_user", "secret_sauce")

    product_page = ProductPage(page)
    product_page.add_to_cart()
    product_page.access_to_cart_page()

    cart_page = CartPage(page)
    cart_page.check_labels_and_buttons()
    cart_page.access_to_checkout_page()

    checkout_information_page = CheckoutInformationPage(page)
    checkout_information_page.fill_fields()
    checkout_information_page.access_checkout_confirmation_page()

    checkout_overview_page = CheckoutOverviewPage(page)
    checkout_overview_page.check_labels_and_buttons()


