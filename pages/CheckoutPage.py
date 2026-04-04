from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        print("CheckoutPage")
        self.page = page

        # locators
        self.first_name = page.get_by_placeholder("First Name")
        self.last_name = page.get_by_placeholder("Last Name")
        self.zip_code = page.get_by_placeholder("Zip/Postal Code")



