import re

# verify()
#
# @param {string} isbn: ISBN to be verified, with or without separating dashes.
def verify(isbn):
    if not isbn: return False
    clean_isbn = re.sub('[^0-9X]', '', isbn)
    if len(clean_isbn) != 10: return False
    if re.search(r'X.+', clean_isbn): return False
    res = 0

    for i in range(9):
        res += int(clean_isbn[i]) * (10 - i)
    if clean_isbn[9] == 'X':
        res += 10
    else:
        res += int(clean_isbn[9])

    return res % 11 == 0
