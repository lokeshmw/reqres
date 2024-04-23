import requests


class BasePage:
    def __init__(self, base_url):
        self.base_url = base_url

    def send_get_request(self, endpoint):
        url = self.base_url + endpoint
        return requests.get(url)

    def send_post_request(self, endpoint, data):
        url = self.base_url + endpoint
        return requests.post(url, json=data)

    def send_put_request(self, endpoint, *data):
        url = self.base_url + endpoint
        return requests.put(url, json=data)

    def send_patch_request(self, endpoint, data):
        url = self.base_url + endpoint
        return requests.patch(url, json=data)

    def send_delete_request(self, endpoint):
        url = self.base_url + endpoint
        return requests.delete(url)
