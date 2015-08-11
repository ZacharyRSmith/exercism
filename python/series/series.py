def slices(digits, size):
    if not size > 0:
        raise ValueError("Your size argument must be an integer > 0")
    if size > len(digits):
        raise ValueError("Your size argument cannot be larger than the "
                         "digits' length!")

    max_start = len(digits) - size

    return [
        [int(n) for n in digits[start:start+size]]
        for start in xrange(max_start+1)
    ]
