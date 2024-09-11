import datetime as dt
import os
from typing import Final

import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN: Final[str] = os.getenv("MY_TOKEN")
USERNAME: Final[str] = os.getenv("MY_USERNAME")
GRAPH = os.getenv("MY_GRAPH")
API_ENDPOINT: Final[str] = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH}"
print(API_ENDPOINT)

now = dt.datetime.now()
date = f"{now:%Y%m%d}"


class PostAPixel:
    def __init__(self):
        self.header = {
            "X-USER-TOKEN": TOKEN
        }
        self.config_pixel = {
            "date": date,
            "quantity": "240",

        }

    def pixel_post(self):
        response = requests.post(API_ENDPOINT, json=self.config_pixel, headers=self.header)
        print(response.text)
