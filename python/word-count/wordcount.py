import re

def word_count(input):
    rslt = {}
    words = re.findall(r'\S+', input)

    for word in words:
        if word in rslt:
            rslt[word] += 1
        else:
            rslt[word] = 1

    return rslt
