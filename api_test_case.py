import unittest
import requests
from config import FULL_ROUTE
import json
from json import JSONDecodeError


class ApiTestCase(unittest.TestCase):
    def request(self, method, path, post_data: dict=None):
        response = requests.request(
            method,
            url=f'{FULL_ROUTE}{path}',
            json=post_data,
            headers={
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'
                'Content-type": "application/json; charset=UTF-8'
            }
        )
        #print(response.content)
        try:
            content = json.loads(response.content.decode())
        except JSONDecodeError:
            content = response.content.decode()

        return response.headers, content