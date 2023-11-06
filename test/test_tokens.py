import pytest
import requests_mock
import json
from playlist_tempo.config.paths import AUTH_URL
from playlist_tempo.config.env import LIVE

from playlist_tempo.tokens import create_token


@requests_mock.Mocker(kw="mock")
def test_create_token(**kwargs):
    file = open("./fakes/data.json")
    json_body = json.load(file)

    if LIVE == True:
        kwargs["mock"].post(f"{AUTH_URL}/token", json=json_body["token"])

    else:
        kwargs["mock"].get(f"{AUTH_URL}/token", json=json_body["token"])

    response = create_token()

    assert response["access_token"] == "helloworld"
