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

        # variables
        payment_info_text = "Payment Information:"
        payment_value_text = "SauceCard #31337"
        shipping_info_text = "Shipping Information:"
        shipping_value_text = "Free Pony Express Delivery!"
        price_info_text = "Price Total"
        subtotal_label_text = "Item total: $29.99"
        tax_label_text = "Tax: $2.40"
        total_label_text = "Total: $32.39"
        cancel_button_text = "Cancel"
        finish_button_text = "Finish"