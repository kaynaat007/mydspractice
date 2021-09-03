"""
not solved March 5th 2021
"""

import math
from typing import List


def util_recursion(stones, i, j, n, prefix_sum):

    if j == i:
        return 0

    if j - i + 1 == 2:
        return min(stones[i], stones[j])

    if i >= n or i < 0:
        return 0

    if j >= n or j < 0:
        return 0

    e = j - i + 1

    max_score = -1 * math.inf
    max_score1 = 0
    max_score2 = 0
    max_score3 = 0
    max_score4 = 0

    for k in range(e-1):
        left_sum = get_sum(prefix_sum, i, i+k, n)
        right_sum = get_sum(prefix_sum, i+k+1, j, n)
        if left_sum < right_sum:
            max_score1 = left_sum + util_recursion(stones, i, i + k, n, prefix_sum)
        elif left_sum > right_sum:
            max_score2 = right_sum + util_recursion(stones, i + k + 1, j, n, prefix_sum)
        else:
            max_score3 = left_sum + util_recursion(stones, i, i + k, n, prefix_sum)
            max_score4 = left_sum + util_recursion(stones, i + k + 1, j, n, prefix_sum)
        max_score = max(max_score, max_score1, max_score2, max_score3, max_score4)

    return max_score


def get_diff(prefix_sum, i, x, y, n):

    left_sum = get_sum(prefix_sum, x, i, n)
    right_sum = get_sum(prefix_sum, i + 1, y, n)
    return left_sum - right_sum


def b_search(prefix_sum, low, high, x, y, n):
    """

    :param prefix_sum:
    :param low:
    :param high:
    :return:
    [2, 5]
    [0, 2, 7]
    [

    """

    if low > high:
        return -1

    if high - low == 0:
        return high

    mid = low + (high - low) // 2

    prev_diff = get_diff(prefix_sum, mid-1, x, y, n)
    curr_diff = get_diff(prefix_sum, mid, x, y, n)

    if curr_diff > 0:
        if prev_diff > 0:
            return b_search(prefix_sum, low, mid-1, x, y, n)
        else:
            return mid
    else:
        return b_search(prefix_sum, mid+1, high, x, y, n)


def util_recursion_top_down(stones, i, j, n, prefix_sum, cache):

    # print(i, j)

    if j == i:
        cache[(i, j)] = 0
        return 0

    if j - i + 1 == 2:
        cache[(i, j)] = min(stones[i], stones[j])
        return min(stones[i], stones[j])

    if i >= n or i < 0:
        return 0

    if j >= n or j < 0:
        return 0

    if (i, j) in cache:
        # print('hit..')
        return cache[(i, j)]

    max_score = -1 * math.inf

    max_score1 = 0
    max_score2 = 0
    max_score3 = 0
    max_score4 = 0

    q = b_search(prefix_sum, i, j, i, j, n)

    for k in [q-1, q, q+1]:

        # print('k between {} and {} is {}'.format(i, j, k))

        if k == 0:
            k = k + 1

        left_sum = get_sum(prefix_sum, i, k-1, n)
        right_sum = get_sum(prefix_sum, k, j, n)

        if left_sum < right_sum:
            max_score1 = left_sum + util_recursion_top_down(stones, i, k-1, n, prefix_sum, cache)
        elif left_sum > right_sum:
            max_score2 = right_sum + util_recursion_top_down(stones, k, j, n, prefix_sum, cache)
        else:
            max_score3 = left_sum + util_recursion_top_down(stones, i, k-1, n, prefix_sum, cache)
            max_score4 = left_sum + util_recursion_top_down(stones, k, j, n, prefix_sum, cache)

        max_score = max(max_score, max_score1, max_score2, max_score3, max_score4)

    cache[(i,j)] = max_score
    return max_score


def get_sum(prefix_sum, i, j, n):

    if i - 1 < 0:
        lower = 0
    else:
        lower = prefix_sum[i-1]

    if j < 0:
        return 0

    upper = prefix_sum[j]

    return upper - lower


def stoneGameV(stoneValue: List[int]) -> int:

    print('---recursion -----')
    n = len(stoneValue)

    prefix_sum = [0 for _ in range(n)]
    diff = [0 for _ in range(n)]
    prefix_sum[0] = stoneValue[0]
    max_score = 0

    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1] + stoneValue[i]

    for i in range(n):
        left_sum = get_sum(prefix_sum, 0, i, n)
        right_sum = get_sum(prefix_sum, i+1, n-1, n)
        diff[i] = left_sum - right_sum

    max_score = util_recursion(stoneValue, 0, n-1, n, prefix_sum)
    print('prefix array: {}'.format(prefix_sum))
    print('diff array: {}'.format(diff))
    index = b_search(prefix_sum, 0, n-1, 0, n-1, n)
    print('index of first positive diff: {} with diff: {}'.format(index, diff[index]))
    # print(max_score)
    return max_score



def stoneGameVTopDown(stoneValue: List[int]) -> int:

    print('---- top down -----')

    n = len(stoneValue)

    prefix_sum = [0 for _ in range(n)]
    prefix_sum[0] = stoneValue[0]

    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1] + stoneValue[i]

    max_score = util_recursion_top_down(stoneValue, 0, n-1, n, prefix_sum, {})
    # print(max_score)
    return max_score



stones = [1,2]
stones = [1]
# stones = [1,2,3]
# stones = [5, 1, 8]
# stones = [6,2,3,4,5,5]

# stones = [7,7,7,7,7,7,7]
# stones = [4, 5, 6, 1, 9, 10]
# stones = [4, 5, 6, 1, 9, 10, 12, 45, 21, 89, 11, 9, 8, 4, 5, 6]
stones = [1, 100, 101, 2, 3, 4]
# stones = [39994,3,4,10000,10000,10000,10000,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1000000]

# stones = [4]
stones = [1,99,1,99,50,50,50,50,1,401,1]

# stones = [6, 2, 3]
print(stoneGameV(stones))


# print(len(stones))
print(stoneGameVTopDown(stones))


