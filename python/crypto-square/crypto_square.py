import math
import re


class CryptoSquare(object):
    """CryptoSquare"""
    def __init__(self, plain_text):
        self.text = self._normalize(plain_text)

    @property
    def value(self):
        res = ''

        for i in range(self.side_len):
            for j in range(self.side_len):
                if j >= len(self.rows) or i >= len(self.rows[j]):
                    continue
                res += self.rows[j][i]
            res += ' '

        return res.strip()

    @property
    def rows(self):
        rows = []
        text = self.text
        while text:
            rows.append(text[:self.side_len])
            text = text[self.side_len:]
        return rows

    @property
    def side_len(self):
        return math.ceil(len(self.text)**(1/2))

    def _normalize(self, plain_text):
        return re.sub(r'\W*', '', plain_text).lower()


def encode(plain_text):
    cryptoSquare = CryptoSquare(plain_text)
    return cryptoSquare.value
