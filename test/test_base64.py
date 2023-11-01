import pytest

from playlist_tempo.utils.base64 import encode


def test_base64_encode():
    assert encode("hello, world") == "aGVsbG8sIHdvcmxk"
