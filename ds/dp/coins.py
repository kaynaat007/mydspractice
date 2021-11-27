def find_combinations(coins, n):
    if len(coins) == 0 and n >= 1:
        return 0
    if n == 0:
        return 1
    if n < 0:
        return 0
    return find_combinations(coins, n-coins[-1]) + find_combinations(coins[0:-1], n)


def find_combinations_dp(coins, n):

    w = [[0] * (n+1)] * len(coins)
    l = len(coins)
    for i in range(l):
        w[i][0] = 1

    for i in range(0, l):
        for j in range(1, n+1):
            # want to achieve j as the sum with coins[0...i] at disposal
            # case when  ith coin is chosen
            if i - 1 <= 0:
                w[i-1][j] = 0
            if n-coins[j] <= 0:
                w[i][n-coins[j]] = 0
            w[i][j] = w[i-1][j] + w[i][n-coins[j]]
    print(w[l-1][n])


print(find_combinations_dp([1,2,3], 4))
