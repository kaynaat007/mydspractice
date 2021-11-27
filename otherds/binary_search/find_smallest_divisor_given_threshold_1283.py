'''
Application of binary search on the answer
'''
from typing import List
import math


def check(divisor, input_arr):

    r = 0
    for e in input_arr:
        r += math.ceil(e/divisor)

    return r


def b_search(arr, low, high, ans, threshold):
    """
    stores answer in array and recurs for a better answer
    """

    if low > high:
        return

    mid = low + (high - low) // 2
    result = check(mid, arr)
    if result > threshold:
        return b_search(arr, mid+1, high, ans, threshold)
    else:
        ans[0] = mid
        return b_search(arr, low, mid-1, ans, threshold)


def smallestDivisor(nums: List[int], threshold: int) -> int:
    """
    binary search the answer from 1 to max element in the array since
    those are only possible divisors.
    for each such answer, need to check if it's valid and then take a decision
    """
    max_e = max(nums)
    ans = [0]
    b_search(nums, 1, max_e, ans, threshold)
    return ans[0]


nums = [1,2,5,9]
threshold = 6

nums = [44,22,33,11,1]
threshold = 5

nums = [21212,10101,12121]
threshold = 1000000

nums = [2,3,5,7,11]
threshold = 11
print(smallestDivisor(nums, threshold))



