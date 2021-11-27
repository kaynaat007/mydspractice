from typing import List
import math


def check(speed, arr, hour, total):

    total_bananas_to_eat = total
    n = len(arr)
    ate_so_far = 0
    i = 0
    while i < n:
        hours_spent = math.ceil(arr[i]/speed)
        hour -= hours_spent
        ate_so_far += arr[i]
        if hour <= 0:
            break
        i += 1
    # print(total_bananas_to_eat, ate_so_far, hour)
    return ate_so_far == total_bananas_to_eat and hour >= 0


def b_search(arr, low, high, ans, hours, total):
    """
    stores answer in array and recurs for a better answer
    """

    if low > high:
        return

    mid = low + (high - low) // 2

    result = check(mid, arr, hours, total)

    if not result:
        return b_search(arr, mid+1, high, ans, hours, total)
    else:
        ans[0] = mid
        return b_search(arr, low, mid-1, ans, hours, total)


def minEatingSpeed(piles: List[int], h: int) -> int:
    low = 1
    high = sum(piles)
    ans = [0]
    hours = h
    b_search(piles, low, high, ans, hours, high)
    return ans[0]


piles = [10, 5]
hours = 2


# piles = [3,6,7,11]
# hours = 8


# piles = [30,11,23,4,20]
# hours = 5

piles = [30,11,23,4,20]
hours = 7

# print(check(45, piles, hours))
print(minEatingSpeed(piles, hours))

