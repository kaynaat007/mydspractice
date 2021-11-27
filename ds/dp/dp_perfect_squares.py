"""

so recurrence is :

Let k be the highest perfect square index less than  given i
(perfect squares are numbered from 1....k)
min_ways of ith number = 1 + min (
              ways by achieving i - kth perfect square,
              ways by achieving i - (k-1)th perfect square,  ...
              ways by achieving i - 1st perfect square)

min_ways of perfect squares are 1 since they are perfect.

say n = 12
so perfect squares are 1, 4, 9 which are less than 12.

min ways of achieving a sum of 12 by these perfect squares will be

ways of achieving 12 - 9 = 3
ways of achieving 12 - 4 = 8
ways of achieving 12 - 1  = 11

take min of these values and add 1. 1 is added to account for subtracting a perfect square from 12 in each of the cases.


"""

import math


def dp_perfect_squares(n):
    """

    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    ways = [0 for _ in range(n+1)]
    for i in range(1, n+1):

        ps = i * i
        if ps <= n:
            ways[ps] = 1

    for i in range(1, n+1):
        min_ways = n + 1
        ps = math.floor(math.sqrt(i))
        while ps >= 1:
            min_ways = min(min_ways, ways[i-ps * ps])
            ps -= 1
        ways[i] = 1 + min_ways

    # print(ways)
    return ways[n]

print(dp_perfect_squares(13))