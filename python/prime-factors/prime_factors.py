MAX_INT = 93819012551
ONE_MILLION = 1 * 1000 * 1000

composites = set()
hasInit = False
primes = [2]


def _init():
    for i in range(3, ONE_MILLION, 2):
        if i in composites:
            continue
        primes.append(i)
        for j in range(i**2, ONE_MILLION, i):
            composites.add(j)


def _calc_next_prime(num):
    for i in range(primes[-1], num + 1, 2):
        if num % i == 0:
            primes.append(i)
            return i


def _get_lowest_factor(num):
    for prime in primes:
        if num % prime == 0:
            return prime


def prime_factors(natural_number):
    global hasInit
    if natural_number > MAX_INT:
        return ValueError(
            f'input must be <= 93819012551 but {natural_number} was given.')
    if natural_number == 1:
        return []
    if not hasInit:
        _init()
        hasInit = True
    factors = []
    while natural_number:
        if natural_number in primes:
            factors.append(natural_number)
            break
        lowest_factor = _get_lowest_factor(natural_number)
        if lowest_factor:
            factors.append(lowest_factor)
            natural_number /= lowest_factor
        else:
            lowest_factor = _calc_next_prime(natural_number)
            factors.append(lowest_factor)
            natural_number /= lowest_factor

    return factors
