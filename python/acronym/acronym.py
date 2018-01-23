import re

def abbreviate(words):
    wordList = re.split(r'\W+', words)
    acronymList = [word[0].upper() for word in wordList]
    return ''.join(acronymList)
