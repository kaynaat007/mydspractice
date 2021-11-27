import math
from datetime import datetime
import heapq


MAX = math.floor(math.pow(10, 5))
PRIME_MAX = math.floor(math.pow(10, 6))
# MAX = 20
# MAX = 200005


def get_primes():

    primes_set = set()
    primes = [True for i in range(PRIME_MAX + 1)]

    for p in range(2, PRIME_MAX + 1):

        if primes[p]:
            for k in range(p * p, PRIME_MAX + 1, p):
                primes[k] = False

    for i in range(1, PRIME_MAX + 1):
        if primes[i]:
            primes_set.add(i)
    return primes_set


def ugly_numbers_v4(n):
    """
    idea is to maintain smallest ugly numbers as a next ugly number.
    1 is smallest.
    next ones are 2, 3, 5.
    pick minimum -- 2
    put next ugly numbers from 2 back to heap to obtain a new minimum among  4, 6, 10, 3, and 5.
    repeat

    use seen() set to not to put duplicate numbers in heap so as to be consistent with counting.

    """

    if n == 0:
        return 0
    q = []
    heapq.heappush(q, 1)
    c = 1
    e = 1
    seen = set()
    seen.add(e)

    while c <= n:
        e = heapq.heappop(q)
        if e * 2 not in seen:
            heapq.heappush(q, e * 2)
            seen.add(e * 2)
        if e * 3 not in seen:
            heapq.heappush(q, e * 3)
            seen.add(e * 3)
        if e * 5 not in seen:
            heapq.heappush(q, e * 5)
            seen.add(e * 5)
        c = c + 1

    return e




t = datetime.now()
# print(ugly_number(n))
# print(ugly_number_v2(n))

n = 1960
# print(ugly_number_v3(n))

print(ugly_numbers_v4(n))

print('time took: {}'.format((datetime.now() - t).total_seconds()))

# print(is_ugly_v2(15))