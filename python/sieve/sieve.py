def sieve(max_num):
    non_primes = {}
    primes = []

    for x in xrange(2, max_num+1):
        if x in non_primes:
            continue
        else:
            for y in filter(lambda y: y % x == 0, xrange(x+1, max_num+1)):
                non_primes[y] = True

            primes.append(x)

    return primes
