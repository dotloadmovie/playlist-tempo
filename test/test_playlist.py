import pytest
import requests_mock
import json
from playlist_tempo.config.paths import BASE_URL
from playlist_tempo.playlist import get_playlist_track_ids


@requests_mock.Mocker(kw="mock")
def test_get_playlist_track_ids(**kwargs):
    file = open("./fakes/data.json")
    json_body = json.load(file)

    kwargs["mock"].get(
        f"{BASE_URL}/playlists/helloworld", json=json_body["playlists"][0]
    )

    tracks = get_playlist_track_ids(playlist_id="helloworld", token="helloworld")

    assert tracks == ["hello", "world"]
