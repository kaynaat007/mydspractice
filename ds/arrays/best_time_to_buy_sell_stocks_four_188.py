from typing import List
import math


def maxProfitCorrectbutTimeLimitExceeded(k, prices):
    """
    exceeds time because of O(k * n2 ) complexity
    """
    n = len(prices)
    table = [[0 for i in range(n)] for _ in range(k)]
    left_low = prices[0]

    for i in range(1, n):

        if prices[i] - left_low > table[0][i-1]:
            table[0][i] = prices[i] - left_low
        else:
            table[0][i] = table[0][i-1]

        if prices[i] < left_low:
            left_low = prices[i]

    for i in range(1, k):
        for j in range(1, n):
            one_less_transaction_value = 0
            for m in range(j):
                if prices[j] - prices[m] + table[i-1][m] > one_less_transaction_value:
                    one_less_transaction_value = prices[j] - prices[m] + table[i-1][m]
            table[i][j] = max(table[i][j-1], one_less_transaction_value)

    # print(table)
    return table[k-1][n-1]


def maxProfitOptimised(k, prices):
    """

    optimised on observation
    for each j, we need to see all   0 <= m < j
    and calculate
    T(i, j) = max(T(i-1, m ) + P[j] - P[m])
    P[j] is constant given a j
    Need to see T(i-1, m) - P[m] only and add a P[j] later.
    This can be stored and calculated before hand for previous k when we are processing current k.
    reduces time complexity to O(n * k)

    """
    n = len(prices)
    if n <= 1:
        return 0
    if k == 0:
        return 0
    table = [[0 for i in range(n)] for _ in range(k)]
    left_low = prices[0]
    max_diff_array = [-1 * math.inf for _ in range(n)]

    for i in range(1, n):

        if prices[i] - left_low > table[0][i - 1]:
            table[0][i] = prices[i] - left_low
        else:
            table[0][i] = table[0][i - 1]

        max_diff_array[i] = max(max_diff_array[i - 1], table[0][i] - prices[i])

        if prices[i] < left_low:
            left_low = prices[i]

    # print(table)
    # print(max_diff_array)

    for i in range(1, k):
        for j in range(1, n):
            one_less_transaction_value = max_diff_array[j] + prices[j]
            table[i][j] = max(table[i][j - 1], one_less_transaction_value)
            max_diff_array[j] = max(max_diff_array[j - 1], table[i][j] - prices[j])
        # print(max_diff_array)

    # print(table)
    return table[k - 1][n - 1]

# prices =  [2, 4, 1]
# k = 2

# prices = [3,2,6,5,0,3]
# k = 3

prices = [8, 9, 10, 3, 4, 14]
k = 2 # expected 13

# prices = [10, 3, 4, 14]
# k = 2
#
# prices = [4, 8, 10, 12]
# k = 2

# prices = [1,2,4,2,5,7,2,4,9,0]
# k = 2

print(maxProfitCorrectbutTimeLimitExceeded(k, prices))
print(maxProfitOptimised(k, prices))

# print(base_case(prices, 4))

