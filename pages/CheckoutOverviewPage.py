from playwright.sync_api import Page


class CheckoutOverviewPage:
    def __init__(self, page: Page):
        print("CheckoutOverviewPage")
        self.page = page

