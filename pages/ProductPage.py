from playwright.sync_api import Page, expect


class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_button = page.locator("#add-to-cart-sauce-labs-backpack")
        self.get_element_cart = page.locator("span[class='shopping_cart_badge']")
        self.cart_button = page.locator("a[class*='shopping']")
        self.remove_product_button = page.locator("#remove-sauce-labs-backpack")
        self.cart_label = page.locator("span[class='title']")

    def add_to_cart(self):
        self.add_to_cart_button.click()
        # check if the "Add to cart" has "Remove" text after the click
        expect(self.remove_product_button).to_have_text("Remove")
        get_remove_text_button = self.remove_product_button.text_content()
        print(f"The text of the button is: {get_remove_text_button}")
        # check if the cart button has the badge with "1" article
        expect(self.get_element_cart).to_have_text("1")
        get_number_article = self.get_element_cart.text_content()
        print(f"The badge text of the article is: {get_number_article}")

    def access_to_cart(self):
        self.cart_button.click()
        # check if the label is correct
        expect(self.cart_label).to_have_text("Your Cart")
        get_cart_text = self.cart_label.text_content()
        print(f"The text of the cart page is: {get_cart_text}")












