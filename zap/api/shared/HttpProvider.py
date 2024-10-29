import requests

class HttpProvider():
    def post(self, url, headers, data):
        headers = {
            'Content-Type': 'application/json',
            **headers
        }
        return requests.post(url, headers=headers, json=data)
