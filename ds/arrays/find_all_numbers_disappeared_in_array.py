from typing import List

def findDisappearedNumbers( nums: List[int]) -> List[int]:

    n = len(nums)
    for i in range(n):
        pos = nums[i]
        if nums[i] < 0:
            pos = -1 * pos
        pos -= 1
        if nums[pos] > 0:
            nums[pos] = -1 * nums[pos]

    print(nums)
    o = []
    for i, e in enumerate(nums):
        if e > 0:
            o.append(i+1)
    return o

nums = [4,3,2,7,8,2,3,1]
nums = [1,1,2,4]
print(findDisappearedNumbers(nums))
