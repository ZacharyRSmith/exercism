def histogram(word):
    res = {}
    for ch in word:
        if ch not in res:
            res[ch] = 0
        res[ch] += 1
    return res


def detect_anagrams(word, words):
    word_histogram = histogram(word.lower())
    word_lowered = word.lower()
    return [w for w in words
            if w.lower() != word_lowered and histogram(w.lower()) == word_histogram]
