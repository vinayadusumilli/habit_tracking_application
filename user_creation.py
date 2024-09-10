import os
from typing import Final

import requests
from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv()

API_ENDPOINT: str = "https://pixe.la/v1/users"
TOKEN: Final[str] = os.getenv("MY_TOKEN")
USERNAME: Final[str] = os.getenv("MY_USERNAME")


class UserCreation:
    """Creating Pixela User Account"""

    def __init__(self):
        self.parameters = {
            "token": TOKEN,
            "username": USERNAME,
            "agreeTermsOfService": "yes",
            "notMinor": "yes",

        }

    def create_user(self):
        """ https post method to create user account"""
        response = requests.post(API_ENDPOINT, json=self.parameters)
        print(response.text)
