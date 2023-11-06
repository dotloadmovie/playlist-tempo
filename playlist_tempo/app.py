from functools import reduce

from playlist_tempo.playlist import get_playlist_track_ids
from playlist_tempo.track import get_track_tempo


def average_tempo(playlist_id):
    ids = get_playlist_track_ids(playlist_id, "helloworld")

    def get_tempo(id):
        return get_track_tempo(id)

    tempos = list(ids.map(get_tempo, ids))

    return reduce(lambda curr, next: curr + next, tempos) / len(tempos)
