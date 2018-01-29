copyAndPaste = [
    (['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'], 1),
    (['D', 'G'], 2),
    (['B', 'C', 'M', 'P'], 3),
    (['F', 'H', 'V', 'W', 'Y'], 4),
    (['K'], 5),
    (['J', 'X'], 8),
    (['Q', 'Z'], 10)
]
letterToScore = {}
for letters, score in copyAndPaste:
    for letter in letters:
        letterToScore[letter] = score


def score(word):
    if not all(ch.isalpha() for ch in word):
        return 0
    return sum(letterToScore[letter.upper()] for letter in word)
