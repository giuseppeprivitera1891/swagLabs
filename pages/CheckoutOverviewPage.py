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
        self.checkout_complete_label = page.locator("span[class='title']")
        self.thanks_for_order = page.locator("h2[class='complete-header']")
        self.order_message = page.locator("div[data-test='complete-text']")
        self.back_home_button = page.get_by_role("button", name="Back Home")

        # variables
        self.payment_info_text = "Payment Information:"
        self.payment_value_text = "SauceCard #31337"
        self.shipping_info_text = "Shipping Information:"
        self.shipping_value_text = "Free Pony Express Delivery!"
        self.price_info_text = "Price Total"
        self.subtotal_label_text = "Item total: $29.99"
        self.tax_label_text = "Tax: $2.40"
        self.total_label_text = "Total: $32.39"
        self.cancel_button_text = "Cancel"
        self.finish_button_text = "Finish"
        self.checkout_complete_text = "Checkout: Complete!"
        self.thanks_for_order.text = "Thank you for your order!"
        self.order_message.text = ("Your order has been dispatched, and will arrive just as fast as the pony can get "
                                   "there!")
        self.back_home_button_text = "Back Home"

    def check_labels_and_buttons(self):
        # checks if the payment information label is correct
        expect(self.payment_info).to_have_text(self.payment_info_text)
        get_payment_info_text = self.payment_info.text_content()
        print(f'Payment Information label is: {get_payment_info_text}')
        # checks if the detail of the payment information is correct
        expect(self.payment_value).to_have_text(self.payment_value_text)
        get_payment_value_text = self.payment_value.text_content()
        print(f'Payment Value label is: {get_payment_value_text}')
        # checks if the shipping information label is correct
        expect(self.shipping_info).to_have_text(self.shipping_info_text)
        get_shipping_info_text = self.shipping_info.text_content()
        print(f'Shipping Info label is: {get_shipping_info_text}')
        # checks if the shipping information value is  correct
        expect(self.shipping_value).to_have_text(self.shipping_value_text)
        get_shipping_value_text = self.shipping_value.text_content()
        print(f'Shipping Value label is: {get_shipping_value_text}')
        # checks if the price total label is correct
        expect(self.price_info).to_have_text(self.price_info_text)
        get_price_info_text = self.price_info.text_content()
        print(f'Price Info label is: {get_price_info_text}')
        # checks if the item total value is correct
        expect(self.subtotal_label).to_have_text(self.subtotal_label_text)
        get_subtotal_label_text = self.subtotal_label.text_content()
        print(f'Subtotal label is: {get_subtotal_label_text}')
        # checks if the tax label is correct
        expect(self.tax_label).to_have_text(self.tax_label_text)
        get_tax_label_text = self.tax_label.text_content()
        print(f'Tax label is: {get_tax_label_text}')
        # checks if the total label is correct
        expect(self.total_label).to_have_text(self.total_label_text)
        get_total_label_text = self.total_label.text_content()
        print(f'Total label is: {get_total_label_text}')
        # checks if the cancel text button is correct
        expect(self.cancel_button).to_have_text(self.cancel_button_text)
        get_cancel_button_text = self.cancel_button.text_content()
        print(f'Cancel button is: {get_cancel_button_text}')
        # checks if the finish text button is correct
        expect(self.finish_button).to_have_text(self.finish_button_text)
        get_finish_button_text = self.finish_button.text_content()
        print(f'Finish button is: {get_finish_button_text}')

    def confirm_order(self):
        self.finish_button.click()
        # checks if the name of the label if correct
        expect(self.checkout_complete_label).to_have_text(self.checkout_complete_text)
        get_checkout_complete_label_text = self.checkout_complete_label.text_content()
        print(f'Checkout complete label is: {get_checkout_complete_label_text}')
