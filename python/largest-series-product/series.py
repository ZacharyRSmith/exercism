from operator import mul


def largest_product(series, size):
    products = map(lambda slic: reduce(mul, slic, 1), slices(series, size))

    return reduce(lambda x, y: max(x, y), products[1:], products[0])


def slices(series, size):
    """ This guard is commented-out because of a silly test:
    if not size > 0:
        raise ValueError("Your size argument must be an integer greater "
                         "than 0! ;_;")
    """
    if size > len(series):
        raise ValueError("Your size argument cannot be larger than the "
                         "series' length. Sneak!")

    max_start = len(series) - size

    return [
        [int(n) for n in series[start:start+size]]
        for start in xrange(max_start+1)
    ]
