import re

CEASAR_SHIFT_BY = 3
ORD_FOR_a = 97
ORD_FOR_z = 122
NUM_LETTERS = 26


def shift(ch, shift_by):
    o = ord(ch) + shift_by
    while o > ORD_FOR_z:
        o -= NUM_LETTERS
    while o < ORD_FOR_a:
        o += NUM_LETTERS
    return chr(o)


class Cipher(object):

    def __init__(self, key='d'*100):
        if re.search(r'[^a-z]', key):
            raise ValueError(f'key must be all lowercase letters, but received "{key}".')
        self.key = key

    def encode(self, text):
        return ''.join(shift(text[i], self._get_shift(i))
                       for i in range(len(text)))

    def decode(self, text):
        return ''.join(shift(text[i], -self._get_shift(i))
                       for i in range(len(text)))

    def _get_shift(self, i):
        while i >= len(self.key):
            i -= len(self.key)
        return ord(self.key[i]) - ORD_FOR_a


class Caesar(object):

    def __init__(self):
        pass

    def decode(self, input):
        return ''.join(shift(ch, -CEASAR_SHIFT_BY) for ch in self._clean(input))

    def encode(self, input):
        return ''.join(shift(ch, CEASAR_SHIFT_BY) for ch in self._clean(input))

    def _clean(self, text):
        return re.sub(r'[^a-zA-Z]', '', text).lower()
