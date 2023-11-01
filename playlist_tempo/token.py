import os

import requests
from utils.base64 import encode

raw = "%s:%s" % (
    os.environ.get("SPOTIFY_CLIENT"),
    os.environ.get("SPOTIFY_SECRET"),
)


print(encode(raw))
