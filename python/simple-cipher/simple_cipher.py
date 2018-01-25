import re
import secrets
import string

CEASAR_SHIFT_BY = 3
ORD_FOR_a = 97
ORD_FOR_z = 122
NUM_LETTERS = 26


def gen_key():
    return ''.join([secrets.choice(string.ascii_lowercase)
                    for i in range(100 + secrets.randbelow(50))])


def shift(ch, shift_by):
    o = ord(ch) + shift_by
    while o > ORD_FOR_z:
        o -= NUM_LETTERS
    while o < ORD_FOR_a:
        o += NUM_LETTERS
    return chr(o)


def clean(text):
    return re.sub(r'[^a-zA-Z]', '', text).lower()


class Cipher(object):
    def __init__(self, key=gen_key()):
        if not all(ch.isalpha() and ch.islower() for ch in key):
            raise ValueError(f'key must be all lowercase letters, but received "{key}".')
        self.secret = key

    @property
    def key(self):
        return self.secret

    def encode(self, input):
        cleaned = clean(input)
        return ''.join(shift(cleaned[i], self._get_shift(i))
                       for i in range(len(cleaned)))

    def decode(self, text):
        return ''.join(shift(text[i], -self._get_shift(i))
                       for i in range(len(text)))

    def _get_shift(self, i):
        i = i % len(self.key) if i >= 0 else i % -len(self.key)
        return ord(self.key[i]) - ORD_FOR_a


class Caesar(object):
    def __init__(self):
        self.cipher = Cipher('d')

    def decode(self, input):
        return self.cipher.decode(input)

    def encode(self, input):
        return self.cipher.encode(input)
