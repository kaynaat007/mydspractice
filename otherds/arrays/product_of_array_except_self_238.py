"""
reuse the space of output array to save space.
left and right define properly. 
"""

from typing import List
from functools import reduce

def with_division(nums):

    output = []
    n = len(nums)
    right = 1
    left = 1
    for e in reversed(nums):
        right = right * e
        output.append(right)

    output = list(reversed(output))

    for i in range(len(nums)):

        right = output[i+1] if i + 1 < n else 1
        output[i] = right * left
        left = left * nums[i]

    return output


def productExceptSelf(nums: List[int]) -> List[int]:

    return with_division(nums)


nums = [1,2,3,4]
# nums = [4, 3 , 9, 1]
# nums = [4, 3, 9, 0]
# nums = [0, 0]
# nums = [3, 2, 0, 4]
print(productExceptSelf(nums))
