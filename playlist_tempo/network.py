import requests

URL_PREFIX = "https://api.spotify.com"


def get_playlist(playlist_id):
    playlist = requests.get(URL_PREFIX + "/playlist/" + playlist_id)
    return playlist.json()
