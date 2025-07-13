from pages.import_api import PersonAPI
import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    return "https://api.test.worldsys.ar"


@pytest.fixture(scope="session")
def token(base_url):
    # make a post request to obtain a token
    payload = {"username": "username", "password": "password"}
    response = requests.post(f"{base_url}/auth", json=payload)
    response_json = response.json()
    token = response_json["token"]
    return token


@pytest.fixture
def person_api(base_url, token):
    return PersonAPI(base_url, token)