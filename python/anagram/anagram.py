def _are_same_chars(strA, strB):
    strA_chars = list(strA)
    strA_chars.sort()
    strB_chars = list(strB)
    strB_chars.sort()

    return strA_chars == strB_chars


def detect_anagrams(word, candidates):
    word = word.lower()
    anagrams = []

    for c in candidates:
        c_orig = c
        c = c.lower()

        if c == word:
            continue

        if _are_same_chars(word, c):
            anagrams.append(c_orig)

    return anagrams
