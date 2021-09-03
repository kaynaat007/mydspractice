


def count_primes(n):
    """

    """
    primes = [True for _ in range(n)]
    primes[0] = False
    primes[1] = False
    for p in range(2, int(n ** 0.5 + 1)):

        if primes[p]:
            for k in range(p * p, n, p):
                primes[k] = False

    return len(list(filter(lambda x: x == True, primes)))


n = 3
print(count_primes(n))