from collections import Counter


def is_anagram(a, b):
    return a.lower() != b.lower() and Counter(a.lower()) == Counter(b.lower())


def detect_anagrams(word, words):
    'Returns each word in @words that is an anagram of @word.'
    return [w for w in words if is_anagram(w, word)]
