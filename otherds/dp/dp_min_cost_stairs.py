

def dp_min_cost_stairs(cost):
    """
    """
    n = len(cost)
    if n == 1 or n == 2:
        return 0
    min_cost_dp = [0 for _ in range(n+1)]
    min_cost_dp[0] = 0
    min_cost_dp[1] = 0
    for i in range(2, n+1):
        min_cost_dp[i] = min(cost[i-1] + min_cost_dp[i-1], cost[i-2] + min_cost_dp[i-2])
    return min_cost_dp[n]

cost = [10, 15]
# cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(dp_min_cost_stairs(cost))

