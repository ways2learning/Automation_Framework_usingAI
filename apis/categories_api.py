from apis.base_api import BaseAPI

class CategoriesAPI(BaseAPI):
    def __init__(self, base_url: str):
        super().__init__(base_url)

    def get_all_categories(self):
        """
        Endpoint: /categories
        Method: GET
        Returns the list of all categories and subcategories.
        """
        return self.get("/categories")
