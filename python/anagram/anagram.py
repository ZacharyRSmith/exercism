def detect_anagrams(word, candidates):
    anagrams = []

    for c in candidates:
        if (c.lower() != word.lower()):
            if sorted(c.lower()) == sorted(word.lower()):
                anagrams.append(c)

    return anagrams
