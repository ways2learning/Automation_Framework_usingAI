from apis.base_api import BaseAPI

class UserAPI(BaseAPI):
    def __init__(self, base_url: str, session):
        super().__init__(base_url, session)

    def create_account(self, name: str, email: str, password: str):
        """
        Endpoint: /createAccount
        Params: name, email, password
        """
        data = {
            "name": name,
            "email": email,
            "password": password
        }
        return self.post("/createAccount", data=data)

    def verify_login(self, email: str, password: str):
        """
        Endpoint: /verifyLogin
        Params: email, password
        """
        data = {
            "email": email,
            "password": password
        }
        return self.post("/verifyLogin", data=data)

    def delete_account(self, email: str):
        """
        Endpoint: /deleteAccount
        Params: email
        """
        data = {
            "email": email
        }
        return self.delete("/deleteAccount", data=data)

    def get_user_detail_by_email(self, email: str):
        """
        Endpoint: /getUserDetailByEmail
        Params: email
        """
        params = {
            "email": email
        }
        return self.get("/getUserDetailByEmail", params=params)
