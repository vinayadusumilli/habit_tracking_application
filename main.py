import os

import requests
from dotenv import load_dotenv  # pip install python-dotenv

from user_creation import UserCreation
from graph_creation import GraphCreation

create_user = UserCreation()
create_graph = GraphCreation()

load_dotenv()

#  Token and Username from environment
TOKEN = os.getenv("MY_TOKEN")
USERNAME = os.getenv("MY_USERNAME")

# Creating Pixela User Account if it's not exists
url = f"https://pixe.la/@{USERNAME}"
response = requests.get(url)
if response.status_code != 200:
    create_user.create_user()
else:
    print("This user already exist, please continue to access your account or create new account")
create_graph.create_graph()
