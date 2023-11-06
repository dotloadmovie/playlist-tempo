from playlist_tempo.config.env import LIVE

BASE_URL = "http://localhost:3000"
AUTH_URL = BASE_URL

if LIVE == True:
    BASE_URL = "https://api.spotify.com/v1"
    AUTH_URL = "https://accounts.spotify.com/api"
