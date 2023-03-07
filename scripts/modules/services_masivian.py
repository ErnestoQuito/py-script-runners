import requests
import base64
import json

class MasivBasicApi:
    url: str
    username: str
    password: str

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

    def send_masiv_email(self, content):
        username_password = base64.b64encode(f'{self.username}:{self.password}'.encode(encoding='utf-8'))
        headers = {
            'Authorization': f'Basic {username_password.decode(encoding="utf-8")}',
            'Content-Type': 'application/json'
        }
        response = requests.post(self.url, headers=headers, json=content)
        return json.loads(response.json())
