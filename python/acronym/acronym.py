import re


def abbreviate(words: str) -> str:
    return ''.join(word[0] for word in re.split('\W*', words)).upper()
