import os

import requests
from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv()


# Creating Pixela User Account
class UserCreation:
    def __init__(self):
        self.API_ENDPOINT: str = "https://pixe.la/v1/users"
        self.parameters = {
            "token": os.getenv("MY_TOKEN"),
            "username": os.getenv("MY_USERNAME"),
            "agreeTermsOfService": "yes",
            "notMinor": "yes",

        }

    # https post method to create user account
    def create_user(self):
        response = requests.post(self.API_ENDPOINT, json=self.parameters)
        print(response.text)
