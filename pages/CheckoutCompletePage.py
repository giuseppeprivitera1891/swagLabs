from playwright.sync_api import Page, expect


class CheckoutCompletePage:
    def __init__(self, page: Page):
        print("CheckoutCompletePage")
        self.page = page

        # locators
        self.thanks_for_order = page.locator("h2[class='complete-header']")
        self.order_message = page.locator("div[data-test='complete-text']")
        self.back_home_button = page.get_by_role("button", name="Back Home")
        self.product_label = page.locator("span[class='title']")

        # variables
        self.thanks_for_order_text = "Thank you for your order!"
        self.order_message_text = ("Your order has been dispatched, and will arrive just as fast as the pony can get "
                                   "there!")
        self.back_home_button_text = "Back Home"
        self.product_label_text = "Products"

    def check_messages_and_button(self):
        # checks id the thank order message text is correct
        expect(self.thanks_for_order).to_have_text(self.thanks_for_order_text)
        get_thanks_for_order_text = self.thanks_for_order.text_content()
        print(f"The confirmation message for the order text is: {get_thanks_for_order_text}")
        # checks if the order message text is correct
        expect(self.order_message).to_have_text(self.order_message_text)
        get_order_message_text = self.order_message.text_content()
        print(f"The order message text is: {get_order_message_text}")
        # checks if the back home button text is correct
        expect(self.back_home_button).to_have_text(self.back_home_button_text)
        get_home_button_text = self.back_home_button.text_content()
        print(f"The back home button is: {get_home_button_text}")

    def back_home(self):
        self.back_home_button.click()
        # checks if the user backs to home page
        expect(self.product_label).to_have_text(self.product_label_text)
        get_product_label_text = self.product_label.text_content()
        print(f"The product label text is: {get_product_label_text}")



