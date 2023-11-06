import os

import requests
from playlist_tempo.utils.base64 import encode
from playlist_tempo.config.paths import BASE_URL
from playlist_tempo.config.env import LIVE


def create_token():
    raw = "%s:%s" % (
        os.environ.get("SPOTIFY_CLIENT"),
        os.environ.get("SPOTIFY_SECRET"),
    )

    key = encode(raw)

    headers = {
        "Authorization": "Basic " + key,
        "Content-Type": " application/x-www-form-urlencoded",
    }
    data = {"grant_type": "client_credentials"}

    if LIVE == True:
        response = requests.post(BASE_URL + "/token", headers=headers, data=data)
    else:
        response = requests.get(
            BASE_URL + "/token",
        )

    return response.json()
