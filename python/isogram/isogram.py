import re

def is_isogram(input = ''):
    if (not input): return True
    input = re.sub(r'\_*\W*\d*', '', input).lower()

    s = set(input[0])
    for ch in input[1:]:
        if (ch in s): return False
        s.add(ch)

    return True
