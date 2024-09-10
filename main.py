import os

import requests
from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv()

# Creating Pixela User Account
API_ENDPOINT: str = "https://pixe.la/v1/users"
parameters = {
    "token": os.getenv("MY_TOKEN"),
    "username": os.getenv("MY_USERNAME"),
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}
# https post method to create user account
response = requests.post(API_ENDPOINT, json=parameters)
print(response.text)

