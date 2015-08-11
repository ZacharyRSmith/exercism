def detect_anagrams(word, candidate_list):
    return filter(lambda c: (word.lower() != c.lower()) and
                  (sorted(word.lower()) == sorted(c.lower())), candidate_list)
