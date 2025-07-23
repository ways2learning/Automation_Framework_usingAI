from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.cart_items = ".cart_info"
        self.checkout_btn = ".check_out"

    def is_cart_items_visible(self):
        return self.page.is_visible(self.cart_items)

    def proceed_to_checkout(self):
        self.page.click(self.checkout_btn)

    def get_title(self):
        return self.page.title()

    def is_cart_empty_text_present(self):
        # This assumes the cart empty message has a unique text
        return self.page.locator("//*[contains(text(), 'Cart is empty!')]").is_visible()