import typing
from collections import Counter


def is_anagram(a: str, b: str) -> bool:
    return a.lower() != b.lower() and Counter(a.lower()) == Counter(b.lower())


def detect_anagrams(word: str, words: typing.Iterable[str]) -> typing.List[str]:
    'Returns each word in @words that is an anagram of @word.'
    return [w for w in words if is_anagram(w, word)]
