from apis.base_api import BaseAPI

class SearchAPI(BaseAPI):
    def __init__(self, base_url, session):
        super().__init__(base_url, session)

    def search_product(self, query: str):
        """
        Perform product search with a query string.
        """
        endpoint = f"/searchProduct"
        payload = {"search_product": query}
        return self.post(endpoint, data=payload)