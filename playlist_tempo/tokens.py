import os

import requests
from playlist_tempo.utils.base64 import encode
from playlist_tempo.config.paths import BASE_URL


def create_token():
    raw = "%s:%s" % (
        os.environ.get("SPOTIFY_CLIENT"),
        os.environ.get("SPOTIFY_SECRET"),
    )

    key = encode(raw)

    headers = {"Authorization": "Basic " + key}

    response = requests.get(
        BASE_URL + "/token",
    )

    return response.json()
