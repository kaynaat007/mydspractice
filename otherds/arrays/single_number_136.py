from typing import List

def singleNumber(nums: List[int]) -> int:

    x = 0
    for e in nums:
        x = x ^ e
    return x

# nums = [2,2,1]
nums = [4,1,2,1,2]
nums = [1]
nums = [-1, -2, 3, -2, -1]
print(singleNumber(nums))



