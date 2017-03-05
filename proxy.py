import requests

class ApiProxy:
    def __init__(self, url):
        self.url = url
        pass

    def get(self):
        return requests.get(self.url)

    def post(self, params):
        return requests.post(self.url, json=params)

    def put(self, params):
        return requests.put(self.url, json=params)

    def delete(self):
        return requests.delete(self.url)
