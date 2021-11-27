from typing import List


def util(stones, prefix_sum, i, j, n):

    if j < i:
        return 0

    if j - i + 1 == 2:
        return max(stones[i], stones[j])

    if i == j:
        return 0

    return max(get_sum(prefix_sum, i+1, j, n) - util(stones, prefix_sum, i+1, j, n),
               get_sum(prefix_sum, i, j-1, n) - util(stones, prefix_sum, i, j-1, n))


def util_top_down_cache(stones, prefix_sum, i, j, n, cache):

    if (i, j) in cache:
        return cache[(i, j)]

    if j < i:
        return 0

    if j - i + 1 == 2:
        cache[(i, j)] = max(stones[i], stones[j])
        return max(stones[i], stones[j])

    if i == j:
        cache[(i, j)] = 0
        return 0

    max_diff =  max(get_sum(prefix_sum, i+1, j, n) - util_top_down_cache(stones, prefix_sum, i+1, j, n, cache),
               get_sum(prefix_sum, i, j-1, n) - util_top_down_cache(stones, prefix_sum, i, j-1, n, cache))

    cache[(i, j)] = max_diff
    return max_diff


def util_bottom_up(stones, prefix_sum, n):

    table = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if  i == j:
                table[i][j] = 0
            elif i + 1 == j:
                table[i][j] = max(stones[i], stones[j])

    for l in range(2, n):
        j = l
        for i in range(n-l):

            table[i][j] = max(get_sum(prefix_sum, i+1, j, n) - table[i+1][j], get_sum(prefix_sum, i, j-1, n) - table[i][j-1])
            j += 1

    return table[0][n-1]


def util_bottom_up_linear_space(stones, prefix_sum, n):

    table = [0 for _ in range(n)]
    for i in range(n-1):
        table[i] = max(stones[i], stones[i+1])

    for l in range(2, n):
        j = l
        for i in range(n-l):
            table[i] = max(get_sum(prefix_sum, i+1, j, n) - table[i+1], get_sum(prefix_sum, i, j-1, n) - table[i])
            j += 1

    return table[0]


def get_sum(prefix_sum, i, j, n):

    if i - 1 < 0:
        lower = 0
    else:
        lower = prefix_sum[i-1]

    upper = prefix_sum[j]

    return upper - lower



def stoneGameVII(stones: List[int]) -> int:

     print('--- recursion ---')
     n = len(stones)
     prefix_sum = [0 for _ in range(n)]
     prefix_sum[0] = stones[0]
     for i in range(1, n):
         prefix_sum[i] = prefix_sum[i-1] + stones[i]

     print('prefix: {}'.format(prefix_sum))
     max_diff = util(stones, prefix_sum, 0, n-1, n)
     print(max_diff)
     return max_diff


def stoneGameVIITopDown(stones: List[int]) -> int:

     n = len(stones)
     prefix_sum = [0 for _ in range(n)]
     prefix_sum[0] = stones[0]
     for i in range(1, n):
         prefix_sum[i] = prefix_sum[i-1] + stones[i]

     # print('prefix: {}'.format(prefix_sum))
     max_diff = util_top_down_cache(stones, prefix_sum, 0, n-1, n, {})
     # print(max_diff)
     return max_diff


def stoneGameVIIBottomUp(stones: List[int]) -> int:
    print('---- bottom up -----')
    n = len(stones)
    prefix_sum = [0 for _ in range(n)]
    prefix_sum[0] = stones[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + stones[i]

    # print('prefix: {}'.format(prefix_sum))
    max_diff = util_bottom_up(stones, prefix_sum, n)
    print(max_diff)
    return max_diff

def stoneGameVIIBottomUpLinearSpace(stones: List[int]) -> int:
    print('---- bottom up linear space -----')
    n = len(stones)
    prefix_sum = [0 for _ in range(n)]
    prefix_sum[0] = stones[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + stones[i]

    # print('prefix: {}'.format(prefix_sum))
    max_diff = util_bottom_up_linear_space(stones, prefix_sum, n)
    print(max_diff)
    return max_diff

stones = [1, 2, 3]
stones = [5, 1, 8]
stones = [5, 1, 8, 4]
stones = [5,3,1,4,2]

stones = [7,90,5,1,100,10,10,2]

stoneGameVII(stones)
# stoneGameVIITopDown(stones)
# stoneGameVIIBottomUp(stones)
stoneGameVIIBottomUpLinearSpace(stones)

