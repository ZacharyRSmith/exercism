from operator import mul


def largest_product(series, size):
    return max(reduce(mul, s, 1) for s in slices(series, size))


def slices(series, size):
    """ This guard is commented-out because of a silly test:
    if not size > 0:
        raise ValueError("Your size argument must be an integer greater "
                         "than 0! ;_;")
    """
    if size > len(series):
        raise ValueError("Your size argument cannot be larger than the "
                         "series' length. Sneak!")

    nums = [int(n) for n in series]

    return [nums[i:i+size]
            for i in xrange(len(nums)+1 - size)]
