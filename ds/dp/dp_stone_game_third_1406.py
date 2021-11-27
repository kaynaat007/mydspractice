from typing import List
import math


def util_top_down_maximal_diff_score(stones, stone_prefix_sum, i, n):

    if i == n-1:
        return stones[i]

    if i >= n or i < 0:
        return 0

    max_score_diff = -1 * math.inf
    for x in range(1, 4):

        if i + x >= n:
            upper = stone_prefix_sum[n-1]
        else:
            upper = stone_prefix_sum[i + x - 1]

        if i - 1 < 0:
            lower = 0
        else:
            lower = stone_prefix_sum[i-1]

        curr_score = upper - lower
        max_score_diff = max(max_score_diff, curr_score - util_top_down_maximal_diff_score(stones, stone_prefix_sum, i + x, n))

    return max_score_diff


def util_top_down_maximal_diff_score_top_down(stones, stone_prefix_sum, i, n, cache):

    if i == n-1:
        cache[i] = stones[i]
        return stones[i]

    if i >= n or i < 0:
        return 0

    max_score_diff = -1 * math.inf
    if i in cache:
        # print('hit...')
        return cache[i]

    for x in range(1, 4):

        if i + x >= n:
            upper = stone_prefix_sum[n-1]
        else:
            upper = stone_prefix_sum[i + x - 1]

        if i - 1 < 0:
            lower = 0
        else:
            lower = stone_prefix_sum[i-1]

        curr_score = upper - lower
        remaining_score = util_top_down_maximal_diff_score_top_down(stones, stone_prefix_sum, i + x, n, cache)
        if curr_score - remaining_score > max_score_diff:
            max_score_diff = curr_score - remaining_score

    cache[i] = max_score_diff

    return max_score_diff


def util_top_down_maximal_diff_score_bottom_up(stones, stone_prefix_sum, i, n):

    max_diff_table = [0 for _ in range(n+1)]
    max_diff_table[n-1] = stones[n-1]

    for i in range(n-2, -1, -1):

        max_score_diff = -1 * math.inf

        for x in range(1, 4):

            if i + x >= n:
                upper = stone_prefix_sum[n-1]
            else:
                upper = stone_prefix_sum[i + x - 1]

            if i - 1 < 0:
                lower = 0
            else:
                lower = stone_prefix_sum[i-1]

            curr_score = upper - lower

            k = min(i+x, n)

            remaining_score = max_diff_table[k]

            if curr_score - remaining_score > max_score_diff:
                max_score_diff = curr_score - remaining_score
        max_diff_table[i] = max_score_diff

    # print("max diff table", max_diff_table)

    return max_diff_table[0]




def stoneGameIII(stoneValue: List[int]) -> str:
    print('----recursion----')
    n = len(stoneValue)
    stone_prefix_sum = [0 for _ in range(n)]
    stone_prefix_sum[0] = stoneValue[0]
    for i in range(1, n):
        stone_prefix_sum[i] =  stone_prefix_sum[i-1] + stoneValue[i]
    # print(stone_prefix_sum)
    max_diff_score = util_top_down_maximal_diff_score(stoneValue, stone_prefix_sum, 0, n)
    print("recursion", max_diff_score)
    if max_diff_score == 0:
        return "Tie"
    elif max_diff_score > 0:
        return "Alice"
    else:
        return "Bob"

def stoneGameIIITopDown(stoneValue: List[int]) -> str:
    n = len(stoneValue)
    stone_prefix_sum = [0 for _ in range(n)]
    stone_prefix_sum[0] = stoneValue[0]
    for i in range(1, n):
        stone_prefix_sum[i] =  stone_prefix_sum[i-1] + stoneValue[i]
    print(stone_prefix_sum)
    max_diff_score = util_top_down_maximal_diff_score_top_down(stoneValue, stone_prefix_sum, 0, n, {})
    # print('top down --> ',  max_diff_score)
    if max_diff_score == 0:
        return "Tie"
    elif max_diff_score > 0:
        return "Alice"
    else:
        return "Bob"


def stoneGameIIIBottomUp(stoneValue: List[int]) -> str:
    # print('----bottom up----')
    n = len(stoneValue)
    stone_prefix_sum = [0 for _ in range(n)]
    stone_prefix_sum[0] = stoneValue[0]
    for i in range(1, n):
        stone_prefix_sum[i] =  stone_prefix_sum[i-1] + stoneValue[i]
    # print(stone_prefix_sum)
    max_diff_score = util_top_down_maximal_diff_score_bottom_up(stoneValue, stone_prefix_sum, 0, n)
    # print("bottom-up", max_diff_score)

    # print('top down --> ',  max_diff_score)
    if max_diff_score == 0:
        return "Tie"
    elif max_diff_score > 0:
        return "Alice"
    else:
        return "Bob"

stonValue = [1, 2]

stonValue = [1, 2, 3]

stonValue = [1,2,3,7]

stonValue = [1,2,3,-9]

stonValue = [1,2,3,6]

stonValue = [1,2,3,-1,-2,-3,7]

stonValue = [-1,-2,-3]

print(stoneGameIII(stonValue))
# print(stoneGameIIITopDown(stonValue))
print(stoneGameIIIBottomUp(stonValue))



