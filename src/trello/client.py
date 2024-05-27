import json

import requests

from src import settings


class TrelloClient:
    """
    Trello Client Class

    Initialized with TRELLO_BASE_URL, TRELLO_API_KEY, TRELLO_TOKEN and TRELLO_BOARD_ID.
    """

    def __init__(self):
        self.base_url = settings.TRELLO_BASE_URL
        self.key = settings.TRELLO_API_KEY
        self.token = settings.TRELLO_TOKEN
        self.board_id = settings.TRELLO_BOARD_ID

        self.base_params = {
            'key': self.key,
            'token': self.token,
        }

    def send_request(self, method='GET', url=None, data=None):
        url = self.base_url + url
        response = requests.request(method, url, params=data)
        return response

    def create_list(self, name):
        query = {**self.base_params, 'idBoard': self.board_id, 'name': name}
        response = self.send_request('POST', 'lists', query)
        return response

    def create_card(self, list_id, name):
        query = {**self.base_params, 'idList': list_id, 'name': name}
        response = self.send_request('POST', 'cards', query)
        return response


if __name__ == '__main__':
    client = TrelloClient()
    response = client.create_list('Kol-Tor')
    list_data = response.json()
    print(list_data)

    list_id = list_data['id']
    response = client.create_card(list_id, '1. Alina 0772162342')
    print(response.json())
    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
