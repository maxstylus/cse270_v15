import pytest
import requests

# ChatGPT Prompt: 
# create an integration test using python and pytest
# that calls the endpoint http://127.0.0.1:8000/users/?username=admin&password=qwerty. 
# Verify the response is HTTP code 200. 

def test_user_endpoint_200():
    url = "http://127.0.0.1:8000/users/"
    params = {"username": "admin", "password": "qwerty"}
    response = requests.get(url, params=params)
    
    assert response.status_code == 200

# ChatGPT Prompt:
# create an integration test using python and pytest 
# that calls the endpoint http://127.0.0.1:8000/users/?username=admin&password=admin. 
# Verify the response is HTTP code 401.

def test_user_endpoint_401():
    url = "http://127.0.0.1:8000/users/"
    params = {"username": "admin", "password": "admin"}
    response = requests.get(url, params=params)
    
    assert response.status_code == 401