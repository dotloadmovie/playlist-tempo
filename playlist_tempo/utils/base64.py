import base64


def encode(raw):
    str = raw.encode("ascii")

    encoded = base64.b64encode(str)

    return encoded.decode("ascii")
