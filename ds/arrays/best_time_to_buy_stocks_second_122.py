from typing import List


def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    max_profit = 0
    curr_max = 0
    if n == 1:
        return 0
    last_max_value = prices[n-1]
    for i in range(n-2, -1, -1):

        if prices[i] < prices[i+1]:
            delta = last_max_value - prices[i]
            if delta > curr_max:
                curr_max = delta
        else:
            last_max_value = prices[i]
            max_profit = max_profit + curr_max
            curr_max = 0

    max_profit = max_profit + curr_max
    return max_profit


prices = [2, 3, 7]
prices = [1,2,3,4,5]
prices = [7,6,4,3,1]
prices = [7,1,5,3,6,4]
prices = [2, 8, 20 ,40]
prices = [10, 8, 30, 35, 10, 1, 20]
print(maxProfit(prices))






