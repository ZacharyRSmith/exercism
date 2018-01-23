import string

ALPHABET = string.ascii_lowercase
ALPHABET_SIZE = len(ALPHABET)

def rotate(text: str, key: int) -> str:
    # print(ord('a')) # 97
    # print(ord('z')) # 122
    # print(ord('A')) # 65
    # print(ord('Z')) # 90
    res = ''
    def shouldWrap(o):
        isLowerCase = o <= 90
        return (isLowerCase and o + key > 90) or (not isLowerCase and o + key > 122)

    for ch in text:
        if not ch.isalpha():
            res += ch
            continue
        o = ord(ch)
        if (shouldWrap(o)):
            res += chr(o + key - ALPHABET_SIZE)
        else:
            res += chr(o + key)

    return res
