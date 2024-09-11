import datetime as dt
import os
from typing import Final

import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN: Final[str] = os.getenv("MY_TOKEN")
USERNAME: Final[str] = os.getenv("MY_USERNAME")
GRAPH = os.getenv("MY_GRAPH")
now = dt.datetime.now()
date = f"{now:%Y%m%d}"

API_ENDPOINT: Final[str] = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH}/{date}"


class UpdateAPixel:
    def __init__(self):
        self.header = {
            "X-USER-TOKEN": TOKEN
        }
        self.config_pixel = {
            "quantity": "300",
        }

    def pixel_update(self):
        response = requests.put(API_ENDPOINT, json=self.config_pixel, headers=self.header)
        print(response.text)
