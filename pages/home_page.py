from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.logo_selector = "img[alt='Website for automation practice']"
        self.products_btn = "a[href='/products']"

    def is_logo_visible(self):
        return self.page.is_visible(self.logo_selector)

    def click_products(self):
        self.page.click(self.products_btn)