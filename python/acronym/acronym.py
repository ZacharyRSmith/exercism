import re

def abbreviate(words):
    wordList = re.split(r'\W+', words)
    return ''.join(word[0].upper() for word in wordList)
