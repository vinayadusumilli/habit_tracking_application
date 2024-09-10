import os
from typing import Final

import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN: Final[str] = os.getenv("MY_TOKEN")
USERNAME: Final[str] = os.getenv("MY_USERNAME")
API_ENDPOINT: Final[str] = f"https://pixe.la/v1/users/{USERNAME}/graphs"


class GraphCreation:
    """Creating Graph After User Creation"""
    def __init__(self):
        self.parameters = {
            "id": "codinggraph",
            "name": "Coding",
            "unit": "Minutes",
            "type": "int",
            "color": "ajisai",
        }
        self.header = {
            "X-USER-TOKEN": TOKEN
        }

    def create_graph(self):
        respond = requests.post(url=API_ENDPOINT, json=self.parameters, headers=self.header)
        print(respond.text)
