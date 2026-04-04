from playwright.sync_api import Page


class CheckoutCompletePage:
    def __init__(self, page: Page):
        print("CheckoutCompletePage")
        self.page = page

        # locators
        self.thanks_for_order = page.locator("h2[class='complete-header']")
        self.order_message = page.locator("div[data-test='complete-text']")
        self.back_home_button = page.get_by_role("button", name="Back Home")

        # variables
        self.thanks_for_order_text = "Thank you for your order!"
        self.order_message_text = ("Your order has been dispatched, and will arrive just as fast as the pony can get "
                                   "there!")
        self.back_home_button_text = "Back Home"

