import requests

from playlist_tempo.config.paths import BASE_URL


def get_track_tempo(track_id, token):
    headers = {"Authorization": "Bearer: %s" % (token)}

    response = requests.get(BASE_URL + "/track", headers=headers)

    track = response.json()

    return track["tempo"]
