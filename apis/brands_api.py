from apis.base_api import BaseAPI

class BrandsAPI(BaseAPI):
    def __init__(self, base_url, session):
        super().__init__(base_url, session)

    def get_all_brands(self):
        """
        Returns all brand list available in the store.
        """
        return self.get("/brandsList")