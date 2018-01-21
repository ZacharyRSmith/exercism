import re

# verify()
#
# @param {string} isbn: ISBN to be verified, with or without separating dashes.
def verify(isbn):
    if not isbn: return False
    numbers = [n for n in isbn if n.isdigit()]
    hasX = re.search(r'[\d|-]X{1}$', isbn)
    if len(numbers) != 10:
        if len(numbers) != 9 or not hasX: return False
    res = 0

    for i in range(len(numbers)):
        res = res + int(numbers[i]) * (10 - i)
    if hasX: res += 10

    return res % 11 == 0
