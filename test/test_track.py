import pytest
import requests_mock
import json
from playlist_tempo.config.paths import BASE_URL
from playlist_tempo.track import get_track_tempo


@requests_mock.Mocker(kw="mock")
def test_get_track_tempo(**kwargs):
    file = open("./fakes/data.json")
    json_body = json.load(file)

    kwargs["mock"].get(f"{BASE_URL}/track", json=json_body["track"])

    tempo = get_track_tempo(track_id="helloworld", token="helloworld")

    assert tempo == 118.211
