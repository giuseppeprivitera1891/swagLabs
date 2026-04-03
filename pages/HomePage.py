from playwright.sync_api import Page, expect


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_button = page.locator("#add-to-cart-sauce-labs-backpack")
        self.get_element_cart = page.locator("span[class='shopping_cart_badge']")

    def add_to_cart(self):
        self.add_to_cart_button.click()
        expect(self.get_element_cart).to_have_text("1")
        get_number_article = self.get_element_cart.text_content()
        print(f"The badge text of the article is: {get_number_article}")

