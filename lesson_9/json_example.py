import json
from models import *
users = {
    'user1': 'authenticated',
    'user2': 'вфывыф',
    'user3': 'anonym',
}

json_obj = json.dumps(users, indent=3)

