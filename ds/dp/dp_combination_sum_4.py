from typing import List

def util(target, k, nums, mem):
    """

    :param target:
    :param k:
    :param nums:
    :return:

    W(i, T) = 1 + W(i, T-coins[i]) + W(i-1, T)

    """
    # achieve target 0 with 1 way of not chosing anything
    if target == 0:
        return 1
    if target < 0:
        return 0
    if k < 0:
        return 0

    if (k, target-nums[k]) in mem:
        left = mem[(k, target-nums[k])]
    else:
        left = util(target - nums[k], k, nums, mem)
        mem[(k, target-nums[k])] = left

    if (k-1, target) in mem:
        right = mem[(k-1, target)]
    else:
        right = util(target, k-1, nums, mem)
        mem[(k-1, target)] = right

    return left + right


def coinChange2_leetcode_518_top_down(nums: List[int], target: int):
    """
    Top down approach DP
    """
    n = len(nums)
    mem = {}
    return util(target, n-1, nums, mem)


def coinChange2_leetcode_518_bottom_up(nums: List[int], target: int):
    """
    Top down approach DP
    """
    if not nums:
        return 0

    n = len(nums)
    W = [[0 for j in range(target+1)] for i in range(n)]
    for i in range(n): # for each coin
        for j in range(target+1): # for each possible amount
            # if amount is zero, you can always achieve it by not chosing anything
            if j == 0:
                W[i][j] = 1

    for i in range(n):  # for each coin
        for j in range(1, target + 1):  # for each possible amount
            # chose i th coin or don't chose ith coin
            new_target = j - nums[i]
            ways = 0
            if new_target >= 0:
                ways += W[i][new_target]
            if i-1 >= 0:
                ways += W[i-1][j]
            W[i][j] = ways

    return W[n-1][target]



def combination_sum_leetcode_377_top_down(nums: List[int], target: int, mem):
    """
    Top down approach DP
    """
    if target < 0:
        return 0
    if target == 0:
        return 1

    n = len(nums)

    ways = 0
    for i in range(n):
        t = target - nums[i]
        if t in mem:
            ways += mem[t]
        else:
            from_this = combination_sum_leetcode_377_top_down(nums, target - nums[i], mem)
            mem[t] = from_this
            ways += from_this
    return ways


def combination_sum_leetcode_377_bottom_up(nums: List[int], target: int):
    """
    Top down approach DP
    """
    dp = [0 for i in range(target+1)]
    dp[0] = 1  # achieving a target of 0 is by not chosing any coin
    n = len(nums)
    for i in range(target + 1):  # for each possible target
        for j in range(n):  # for each coin
            t = i - nums[j]  # smaller subproblem target
            if t >= 0:  # make sense only when target > 0
                dp[i] = dp[i] + dp[t]  # check if already have it's solution before hand.
    return dp[-1]


def coinChange2_leetcode_518_bottom_up_2_d_array(nums: List[int], target: int):
    """
    Top down approach DP
    """
    dp =[0 for i in range(target + 1)]
    dp[0] = 1  # achieving 1 by chosing nothing
    for coin in nums: # for all coins
        for j in range(target + 1):  # for all possible targets for each coin
            t = j - coin  # new target.  represents choosing the given coin
            if t >= 0:  # > 0
                dp[j] = dp[j] + dp[t]
    return dp[-1]

nums = [1,2]
target = 3


#
#
# nums = [1, 2, 5]
# target = 5


# #
# nums = [2]
# target = 3


# #
# nums = [10]
# target = 10


#
# nums = [1, 2, 3]
# target = 4

# print(coinChange2_leetcode_518_bottom_up(nums, target))
# print(coinChange2_leetcode_518_top_down(nums, target))
print(combination_sum_leetcode_377_bottom_up(nums, target))
print(coinChange2_leetcode_518_bottom_up_2_d_array(nums, target))





