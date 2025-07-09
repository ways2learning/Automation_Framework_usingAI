from pages.base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def is_products_list_visible(self):
        # Checks if at least one product is displayed on the products page
        return self.page.locator(".features_items .product-image-wrapper").first.is_visible()

    def search(self, query):
        self.page.fill("input#search_product", query)
        self.page.click("button#submit_search")

    def is_search_result_displayed(self):
        # Checks if search results are shown under 'Searched Products'
        return self.page.locator("div.features_items").locator(".product-image-wrapper").first.is_visible()