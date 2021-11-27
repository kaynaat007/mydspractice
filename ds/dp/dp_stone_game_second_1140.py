import math
from typing import List


def util_recursion(m, piles, offset, n, turn):

    if offset == n-1:
        if turn == 1:
            return piles[offset], 0
        return 0, piles[offset]

    if offset >= n:
        return 0, 0

    if turn == 1:
        max_tuple = (0, 0)
        alex_best_score_prev = 0
        # print('alex turn..m = {}, offset: {}'.format(m, offset))
        for x in range(1, 2 * m + 1):
            alex_best_score, bob_best_score = util_recursion(max(m, x), piles, x + offset, n, 2)
            # print('alex best score: {}, bob best score: {}'.format(alex_best_score, bob_best_score))
            score = sum(piles[offset:x+offset])
            if score + alex_best_score > alex_best_score_prev:
                max_tuple = (score + alex_best_score, bob_best_score)
                alex_best_score_prev = score + alex_best_score

        return max_tuple

    if turn == 2:
        max_tuple = (0, 0)
        bob_best_score_prev = 0
        # print('bob turn.. m = {}, offset: {}'.format(m, offset))
        for x in range(1, 2 * m + 1):
            alex_best_score, bob_best_score = util_recursion(max(m, x), piles, x + offset, n, 1)
            # print('alex best score: {}, bob best score: {}'.format(alex_best_score, bob_best_score))
            score = sum(piles[offset:x+offset])
            if score + bob_best_score > bob_best_score_prev:
                max_tuple = (alex_best_score, score + bob_best_score)
                bob_best_score_prev = score + bob_best_score

        return max_tuple



def util_top_down(m, piles, offset, n, turn, cache, sum_cache):

    if offset == n-1:
        if turn == 1:
            cache[(m, offset, turn)] = (piles[offset], 0)
            return piles[offset], 0
        cache[(m, offset, turn)] = (0, piles[offset])
        return 0, piles[offset]

    if offset >= n:
        return 0, 0

    if (m, offset, turn) in cache:
        # print('cache hit..')
        return cache[(m, offset, turn)]

    if turn == 1:
        max_tuple = (0, 0)
        alex_best_score_prev = 0
        # print('alex turn..m = {}, offset: {}'.format(m, offset))
        for x in range(1, 2 * m + 1):
            alex_best_score, bob_best_score = util_top_down(max(m, x), piles, x + offset, n, 2, cache, sum_cache)
            # print('alex best score: {}, bob best score: {}'.format(alex_best_score, bob_best_score))
            # score = sum(piles[offset:x+offset])
            score = get_sum(sum_cache, offset, x+offset-1, n)
            if score + alex_best_score > alex_best_score_prev:
                max_tuple = (score + alex_best_score, bob_best_score)
                alex_best_score_prev = score + alex_best_score

        cache[(m, offset, turn)] = max_tuple
        return max_tuple

    if turn == 2:
        max_tuple = (0, 0)
        bob_best_score_prev = 0
        # print('bob turn.. m = {}, offset: {}'.format(m, offset))
        for x in range(1, 2 * m + 1):
            alex_best_score, bob_best_score = util_top_down(max(m, x), piles, x + offset, n, 1, cache, sum_cache)
            # print('alex best score: {}, bob best score: {}'.format(alex_best_score, bob_best_score))
            # score = sum(piles[offset:x+offset])
            score = get_sum(sum_cache, offset, x+offset-1, n)
            if score + bob_best_score > bob_best_score_prev:
                max_tuple = (alex_best_score, score + bob_best_score)
                bob_best_score_prev = score + bob_best_score

        cache[(m, offset, turn)] = max_tuple
        return max_tuple


def util_without_turn_variable_recursion(piles, sum_cache, i,  m, n):

    if i == n-1:
        return piles[i]

    if i >= n or i < 0:
        return 0
    prev_delta = -1 * math.inf
    for x in range(1, 2 * m + 1):
        prefix_score = get_sum(sum_cache, i, x+i-1, n)
        prev_delta = max(prev_delta, prefix_score - util_without_turn_variable_recursion(piles, sum_cache, x + i, max(m, x), n))
    return prev_delta

def util_without_turn_variable_recursion_with_memo(piles, sum_cache, i,  m, n, cache):

    if i == n-1:
        cache[(m, i)] = piles[i]
        return piles[i]

    if i >= n or i < 0:
        return 0

    if (m, i) in cache:
        return cache[(m, i)]

    prev_delta = -1 * math.inf
    for x in range(1, 2 * m + 1):
        prefix_score = get_sum(sum_cache, i, x+i-1, n)
        prev_delta = max(prev_delta, prefix_score - util_without_turn_variable_recursion_with_memo(piles, sum_cache, x + i, max(m, x), n, cache))

    cache[(m, i)] = prev_delta
    return prev_delta


def util_without_turn_variable_bottom_up(sum_cache,  n):

    table = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(n-1, -1, -1):
        for m in range(n, 0, -1):
            prev_delta = -1 * math.inf # calculate this and store (i, m)
            for x in range(1, 2 * m + 1):

                k = min(n, i + x) # x + i can go far beyond n-1, so putting a cap
                j = min(n, x)  # x can go to 2 * m and we don't have to go till there if array length is just n-1

                # print(m, i, n-i, k)

                if m >= n - i:
                    score = sum_cache[i]
                    prev_delta = score
                    break
                else:
                    if k <= n-1:
                        score = sum_cache[i] - sum_cache[k]
                    else:
                        score = sum_cache[i]
                # print('score: {}'.format(score))
                prev_delta = max(prev_delta, score - table[k][max(m, j)])
            table[i][m] = prev_delta

    # print(table)

    return table[0][1]


def get_sum(sum_cache, i, j, n):
    # print(i, j)
    if i - 1 < 0:
        return sum_cache[j]
    if j >= n:
        j = n - 1
    return sum_cache[j] - sum_cache[i-1]


def get_sum_suffix(sum_cache, i, j, n):
    # print(i, j)
    if i == n-1:
        return sum_cache[j]
    return sum_cache[j] - sum_cache[i+1]


def stoneGameII(piles: List[int]) -> int:

    n = len(piles)
    sum_cache = [0 for i in range(n)]
    sum_cache[0] = piles[0]
    for i in range(1, n):
        sum_cache[i] = piles[i] + sum_cache[i-1]

    alex_best_score, bob_best_score = util_top_down(1, piles, 0, len(piles), 1, {}, sum_cache)
    # print(alex_best_score, bob_best_score)
    return alex_best_score

def stoneGameIIRecursion(piles: List[int]) -> int:

    n = len(piles)
    sum_cache = [0 for i in range(n)]
    sum_cache[0] = piles[0]
    for i in range(1, n):
        sum_cache[i] = piles[i] + sum_cache[i-1]

    alex_best_score, bob_best_score = util_recursion(1, piles, 0, len(piles), 1)
    print('alex: {}'.format(alex_best_score))
    print('diff: {}'.format(alex_best_score - bob_best_score))
    return alex_best_score


def stoneGameIIRecursionRecursionWithoutTurnVariable(piles: List[int]) -> int:

    n = len(piles)
    sum_cache = [0 for i in range(n)]
    sum_cache[0] = piles[0]
    for i in range(1, n):
        sum_cache[i] = piles[i] + sum_cache[i-1]

    optimal_difference = util_without_turn_variable_recursion(piles, sum_cache, 0, 1, n)
    print('optimal diff: {}'.format(optimal_difference))
    total_sum = sum_cache[-1]
    return (total_sum + optimal_difference)//2

def stoneGameIIRecursionRecursionWithoutTurnVariableWithMemo(piles: List[int]) -> int:

    n = len(piles)
    sum_cache = [0 for i in range(n)]
    sum_cache[0] = piles[0]
    for i in range(1, n):
        sum_cache[i] = piles[i] + sum_cache[i-1]

    optimal_difference = util_without_turn_variable_recursion_with_memo(piles, sum_cache, 0, 1, n, {})
    print('optimal diff with memo: {}'.format(optimal_difference))
    total_sum = sum_cache[-1]
    return (total_sum + optimal_difference)//2


def stoneGameIIRecursionRecursionWithoutTurnVariableWithBottomUpDP(piles: List[int]) -> int:

    n = len(piles)
    sum_cache = [0 for i in range(n)]
    sum_cache[n-1] = piles[n-1]
    for i in range(n-2, -1, -1):
        sum_cache[i] = sum_cache[i+1] + piles[i]

    # print(sum_cache)

    optimal_difference = util_without_turn_variable_bottom_up(sum_cache,  n)
    # print('optimal diff with bottom up dp: {}'.format(optimal_difference))
    total_sum = sum_cache[0]
    return (total_sum + optimal_difference)//2


def stoneGameIIBorrowedSol(piles: List[int]) -> int:
    if not piles:
        return 0

    n = len(piles)
    # dp array to store intermediate results
    dp = [[0] * (n + 1) for i in range(n)]

    # compute suffix sum to quickly find the sum of the elements between the two points
    for j in range(n - 2, -1, -1):
        piles[j] += piles[j + 1]

    # for every possible suffix check all possible values of m and x(derived from x)
    # and find optimal solutions for every point.
    # we can have at most n turns, and players at every step are playing optimal = choose x
    # which maximizes the outcome
    for i in range(n - 1, -1, -1):
        for m in range(n, 0, -1):
            print(i, m)
            for x in range(1, 2 * m + 1):
                # both playing optimal, so we either get all elements if go beyond the arrays' limit
                # or have to subtract the best possible value of the next player's move we've seen.
                # the piles[i] suffix sum is the best possible value we can get for any suffix, so we
                # subtract optimal value for suffix [i+x] calculated for the corresponding
                # "next" m =  max(x,m)
                # (remember we are going backwards from the tail)
                val = piles[i] - dp[i + x][max(x, m)] if i + x < n else piles[i]
                dp[i][m] = max(dp[i][m], val)

    print(dp)
    # return the max stones possible for the first player
    return dp[0][1]

piles = [1, 2]
# piles = [2,7,9,4,4]
piles = [1,2,3,4,5,100]
# piles = [1, 2, 3]
# piles = [1, 2, 3, 4]
# piles = [9,2,2,8,3,7,9,9]

# print(stoneGameII(piles))
# print(stoneGameIIRecursion(piles))
# print(stoneGameIIRecursionRecursionWithoutTurnVariable(piles))
# print(stoneGameIIRecursionRecursionWithoutTurnVariableWithMemo(piles))
print(stoneGameIIRecursionRecursionWithoutTurnVariableWithBottomUpDP(piles))
# print(stoneGameIIBorrowedSol(piles))


