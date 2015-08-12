from string import maketrans
import re

trans_tbl = maketrans("abcdefghijklmnopqrstuvwxyz",
                      "zyxwvutsrqponmlkjihgfedcba")


def decode(code):
    return code.replace(' ', '').translate(trans_tbl)


def encode(string):
    return __group(
        re.sub(r'[\W]+', '', string).lower().translate(trans_tbl)
    )


def __group(string):
    if len(string) <= 5:
        return string

    return string[:5] + " " + __group(string[5:])
