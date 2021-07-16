import requests
from key import *

BASE_URL = "https://api.petfinder.com/v2/oauth2/token"

def get_token():
    
    params={"grant_type": "client_credentials", "client_id": petfinder_key, "client_secret": petfinder_secret}
    resp = requests.post(BASE_URL, data=params)

    return resp.json()["access_token"]


