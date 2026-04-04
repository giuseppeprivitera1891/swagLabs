from playwright.sync_api import Page, expect


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
        self.payment_info_text = "Payment Information:"
        self.payment_value_text = "SauceCard #31337"
        self.shipping_info_text = "Shipping Information:"
        self.shipping_value_textshipping_value_text = "Free Pony Express Delivery!"
        self.price_info_text = "Price Total"
        self.subtotal_label_text = "Item total: $29.99"
        self.tax_label_text = "Tax: $2.40"
        self.total_label_text = "Total: $32.39"
        self.cancel_button_text = "Cancel"
        self.finish_button_text = "Finish"

    def check_labels_and_buttons(self):
        # checks if the payment information label is correct
        expect(self.payment_info).to_have_text(self.payment_info_text)
        get_payment_info_text = self.payment_info.text_content()
        print(f'Payment Information label is: {get_payment_info_text}')