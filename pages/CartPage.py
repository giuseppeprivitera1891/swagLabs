from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.product_quantity = page.locator("div[class='cart_quantity']")
        self.product_name = page.locator("div[class='inventory_item_name']")
        self.product_description = page.locator("div[class='inventory_item_desc']")
        self.product_price = page.locator("div[class='inventory_item_price']")
        self.remove_button = page.get_by_role("button", name="Remove")
        self.continue_shopping_button = page.get_by_role("button", name="Continue Shopping")
        self.checkout_button = page.get_by_role("button", name="Checkout")

        self.product_quantity_text = "1"
        self.product_name_text = "Sauce Labs Backpack"
        self.product_description_text = ("carry.allTheThings() with the sleek, '/'"
                                         "streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.")
        self.product_price_text = "$29.99"
        self.remove_button_text = "Remove"
        self.continue_shopping_button_text = "Continue Shopping"
        self.checkout_button_text = "Checkout"

