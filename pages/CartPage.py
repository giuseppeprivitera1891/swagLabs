from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page):
        print("CartPage")
        self.page = page

        # locators
        self.product_quantity = page.locator("div[class='cart_quantity']")
        self.product_name = page.locator("div[class='inventory_item_name']")
        self.product_description = page.locator("div[class='inventory_item_desc']")
        self.product_price = page.locator("div[class='inventory_item_price']")
        self.remove_button = page.get_by_role("button", name="Remove")
        self.continue_shopping_button = page.get_by_role("button", name="Continue Shopping")
        self.checkout_button = page.get_by_role("button", name="Checkout")
        self.checkout_label = page.locator("span[class='title']")

        # variables
        self.product_quantity_text = "1"
        self.product_name_text = "Sauce Labs Backpack"
        self.product_description_text = ("carry.allTheThings() with the sleek, "
                                         "streamlined Sly Pack that melds uncompromising style with unequaled laptop and"
                                         " tablet protection.")
        self.product_price_text = "$29.99"
        self.remove_button_text = "Remove"
        self.continue_shopping_button_text = "Continue Shopping"
        self.checkout_button_text = "Checkout"
        self.checkout_label_text = "Checkout: Your Information"

    def check_labels_and_buttons(self):
        # checks if the quantity of the product is correct
        expect(self.product_quantity).to_have_text(self.product_quantity_text)
        get_quantity_text = self.product_quantity.text_content()
        print(f"The text of the article quantity is: {get_quantity_text}")
        # checks if the name of the product is correct
        expect(self.product_name).to_have_text(self.product_name_text)
        get_name_text = self.product_name.text_content()
        print(f"The text of the article name is: {get_name_text}")
        # checks if the description of the product is correct
        expect(self.product_description).to_have_text(self.product_description_text)
        get_description_text = self.product_description.text_content()
        print(f"The text of the article description is: {get_description_text}")
        # checks if the price of the product is correct
        expect(self.product_price).to_have_text(self.product_price_text)
        get_price_text = self.product_price.text_content()
        print(f"The text of the article price is: {get_price_text}")
        # checks if the name of the remove button is correct
        expect(self.remove_button).to_have_text(self.remove_button_text)
        get_remove_text = self.remove_button.text_content()
        print(f"The text of the remove button is: {get_remove_text}")
        # checks if the name of continue shopping button is correct
        expect(self.continue_shopping_button).to_have_text(self.continue_shopping_button_text)
        get_continue_text = self.continue_shopping_button.text_content()
        print(f"The text of the continue shopping button is: {get_continue_text}")
        # checks if the name of the checkout button is correct
        expect(self.checkout_button).to_have_text(self.checkout_button_text)
        get_checkout_text = self.checkout_button.text_content()
        print(f"The text of the checkout button is: {get_checkout_text}")

    def access_to_checkout_page(self):
        self.checkout_button.click()
        # checks if the title of the page is correct
        expect(self.checkout_label).to_have_text(self.checkout_label_text)
        get_checkout_label_text = self.checkout_label.text_content()
        print(f"The text of the checkout label is: {get_checkout_label_text}")
