import requests
import os
import urllib.parse

# Code writen by Alex Carter from tutorial
# https://towardsdatascience.com/build-your-next-project-with-wolfram-alpha-api-and-python-51c2c361d8b9


class Wolframalpha:
    def __init__(self):
        self.app_id = "48GAJ6-6526YPQVE9"

    def search(self, query: str) -> dict:
        query_parsed = urllib.parse.quote_plus(query)
        query_url = f"http://api.wolframalpha.com/v2/query?appid={self.app_id}&input={query_parsed}&format=plaintext&output=json"
        req = requests.get(query_url).json()
        if req['queryresult']['error']:
            return None
        return req['queryresult']['pods']

    def get_pod(self, search: dict, key: str) -> str:
        for pod in search:
            if pod['title'] == key:
                return pod['subpods']
