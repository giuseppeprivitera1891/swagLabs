from playwright.sync_api import Page


class CheckoutOverviewPage:
    def __init__(self, page: Page):
        print("CheckoutOverviewPage")
        self.page = page

        # locators
        self.payment_info = page.locator("div[data-test='payment-info-label']")
        self.payment_value = page.locator("div[data-test='payment-info-value']")
        self.shipping_info = page.locator("div[data-test='shipping-info-label']")
        self.shipping_value = page.locator("div[data-test='shipping-info-value']")
        self.price_info = page.locator("div[data-test='total-info-label']")
        self.subtotal_label = page.locator("div[data-test='subtotal-label']")
        self.tax_label = page.locator("div[data-test='tax-label']")
        self.total_label = page.locator("div[data-test='total-label']")
        self.cancel_button = page.get_by_role("button", name="Cancel")
        self.finish_button = page.get_by_role("button", name="Finish")

