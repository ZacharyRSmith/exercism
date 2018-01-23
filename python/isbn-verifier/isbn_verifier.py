# verify()
#
# @param {string} isbn: ISBN to be verified, with or without separating dashes.
def verify(isbn):
    if not isbn: return False

    clean_isbn = isbn.replace('-', '')
    if len(clean_isbn) != 10: return False
    # if re.search(r'X.+', clean_isbn): return False
    res = 0

    for digit, coef in zip(clean_isbn, range(10, 0, -1)):
        if not digit.isdigit(): return False
        res += int(digit) * coef
    if clean_isbn[9] == 'X':
        res += 10
    else:
        res += int(clean_isbn[9])
    print(res)
    return res % 11 == 0

print(verify('3-598-21508-8'))
