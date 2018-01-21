def is_isogram(string = ''):
    if (not string): return True
    letters = [c for c in string.lower() if c.isalpha()]

    s = set(letters[0])
    for ch in letters[1:]:
        if (ch in s): return False
        s.add(ch)

    return True
