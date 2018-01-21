from functools import reduce
import re

def abbreviate(words: str) -> str:
    wordList = re.split(r'\W+', words)
    return reduce(lambda x, y: x + y[0].upper(), wordList, '')
