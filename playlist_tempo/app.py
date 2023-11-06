from functools import reduce

from playlist_tempo.tokens import create_token
from playlist_tempo.playlist import get_playlist_track_ids
from playlist_tempo.track import get_track_tempo


def average_tempo(playlist_id):
    token = create_token()
    ids = get_playlist_track_ids(playlist_id, token["access_token"])

    def get_tempo(id):
        return get_track_tempo(id, token["access_token"])

    tempos = list(map(get_tempo, ids))

    return reduce(lambda curr, next: curr + next, tempos) / len(tempos)
