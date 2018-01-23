def is_isogram(string = ''):
    for i in range(ord('a'), ord('z')):
        if string.lower().count(chr(i)) > 1: return False
    return True
