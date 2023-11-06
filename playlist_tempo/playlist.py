import requests

from playlist_tempo.config.paths import BASE_URL


def get_playlist_track_ids(playlist_id, token):
    headers = {"Authorization": "Bearer %s" % (token)}

    response = requests.get(BASE_URL + "/playlists/" + playlist_id, headers=headers)

    playlist = response.json()

    def get_id(track):
        return track["track"]["id"]

    track_ids = map(get_id, playlist["tracks"]["items"])

    return list(track_ids)
