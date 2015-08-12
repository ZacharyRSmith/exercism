from string import ascii_letters, ascii_lowercase, maketrans
import re

ATBASH = maketrans(ascii_letters, 2*(ascii_lowercase[::-1]))


def decode(code):
    return code.translate(ATBASH, ' ')


def encode(string):
    s = re.sub(r'[\W]+', '', string).translate(ATBASH)

    return ' '.join([s[i:i + 5] for i in range(0, len(s), 5)])
