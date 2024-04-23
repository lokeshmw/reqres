from features.pages.Base_page import BasePage


class APIFunctions(BasePage):
    def __init__(self, requests):
        super().__init__("https://reqres.in/api")
        self.requests = requests

    def get_users(self):
        return self.send_get_request("/users")

    def get_user_by_id(self, user_id):
        return self.send_get_request(f"/users/{user_id}")

    def create_user(self, *user_data):
        return self.send_post_request("/users", user_data)

    def Update_user(self, user_id, user_data):
        return self.send_put_request(f"/users/{user_id}", user_data)

    def Delete_user(self, user_id):
        return self.send_delete_request(f"/users/{user_id}")
