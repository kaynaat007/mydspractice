from typing import List


def maxProfit(prices: List[int]) -> int:

    n = len(prices)
    max_profit = 0
    if n == 1:
        return 0

    left_max_diff = [0 for i in range(n)]
    right_max_diff = [0 for i in range(n+1)]
    right_max_diff[n-1] = 0
    left_min_val = prices[0]
    right_max_val = prices[n-1]

    for i in range(1, n):
        if prices[i] > left_min_val:
            left_max_diff[i] = max(left_max_diff[i-1], prices[i] - left_min_val)
        else:
            left_max_diff[i] = left_max_diff[i-1]
            left_min_val = prices[i]

    for i in range(n-2, -1, -1):
        if prices[i] < right_max_val:
            right_max_diff[i] = max(right_max_diff[i+1], right_max_val - prices[i])
        else:
            right_max_diff[i] = right_max_diff[i+1]
            right_max_val = prices[i]

    # print(left_max_diff)
    # print(right_max_diff)

    for i in range(n):
        current_max = max(left_max_diff[i], right_max_diff[i+1], left_max_diff[i] + right_max_diff[i+1])
        if current_max > max_profit:
            max_profit = current_max

    return max_profit


# prices = [7,1,5,3,6,4]
prices = [3,3,5,0,0,3,1,4]
# prices = [1,2,3,4,5]
# prices = [7,6,4,3,1]
# prices =  [1]
# prices = [8, 1, 3, 4, 6, 7]
# prices = [10, 8, 30, 35, 10, 1, 20]
# prices = [45, 90, 12, 34, 87, 22, 11, 34]
# prices = [0, 1, 1, 0, 0, 1, 1]
# prices = [1,2,4,2,5,7 ,2,4,9,0]

prices = [3,2,6,5,0,3]
prices = [1,7,4,2,11]
print(maxProfit(prices))
