import re


def abbreviate(words):
    return ''.join(word[0] for word in re.split('\W*', words)).upper()
