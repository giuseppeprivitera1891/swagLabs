from playwright.async_api import Page, expect


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_button = page.locator("#add-to-cart-sauce-labs-backpack")
        self.get_element_cart = page.locator("span[class='shopping_cart_badge']")

    def add_to_cart(self):
        self.add_to_cart_button.click()
        get_number_article = self.get_element_cart.text_content()
        print(get_number_article)
        expect(get_number_article).to_contain_text("1")