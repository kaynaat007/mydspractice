from typing import List
import math


def minElements(nums: List[int], limit: int, goal: int) -> int:

    current_sum = sum(nums)
    remaining_sum = goal - current_sum
    if remaining_sum == 0:
        return 0
    if remaining_sum < 0:
        remaining_sum = -1 * remaining_sum
    return math.ceil(remaining_sum/limit)


nums = [1,-1,1]
limit = 3
goal = -4



print(minElements(nums, limit, goal))
