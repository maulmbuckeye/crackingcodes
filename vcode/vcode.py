from itertools import cycle
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def vcode(key, text):
    rotating_key = cycle(key.lower())
    return ''.join([
            encode_char(char, rotating_key)
            for char in text
        ])


def encode_char(char, rot):
    is_lower = char.islower()
    pos = ALPHABET.find(char.lower())
    if pos == -1:
        return char

    shift = ALPHABET.find(next(rot))
    encoded_pos = (pos + shift) % 26
    e = ALPHABET[encoded_pos]
    return e if is_lower else e.upper()