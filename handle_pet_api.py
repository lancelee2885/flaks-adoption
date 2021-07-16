import requests
from key import *
from random import choice

BASE_URL = "https://api.petfinder.com/v2/"

def get_token():
    """Request token from petfinder server"""
    params={"grant_type": "client_credentials", "client_id": petfinder_key, "client_secret": petfinder_secret}
    token_url = f'{BASE_URL}oauth2/token'
    resp = requests.post(token_url, data=params)

    return resp.json()["access_token"]

def get_pets_data(token):
    
    # make a request using the token and secret keys
    
    # get pet name, pet species, pet age, photos
    get_pet_data_url = f'{BASE_URL}animals'
    params = {"limit":100}
    
    resp = requests.get(get_pet_data_url,
                        headers={"Authorization":f"Bearer {token}"}).json()

    animal = choice(resp['animals'])
    
    name = animal['name']
    age = animal['age']
    photo_url = animal['photos'][0]['medium']

    return {"name":name, "age":age, "photo_url":photo_url}
