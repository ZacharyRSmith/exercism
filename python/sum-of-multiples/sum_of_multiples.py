def sum_of_multiples(stop, factors=[3, 5]):
    return sum(n for n in xrange(1, stop) if __is_multiple(n, factors))


def __is_multiple(n, factors):
    return any(n % f == 0
               for f in factors if f)
