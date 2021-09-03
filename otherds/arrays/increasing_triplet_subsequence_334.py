from typing import List
from bisect import bisect_right, bisect_left


def increasingTriplet(nums: List[int]) -> bool:

    n = len(nums)
    if n == 0:
        return False
    tailTable = [0 for i in range(n+1)]
    tailTable[0] = nums[0]
    k = 1
    for i in range(1, n):
        # print(tailTable)
        if nums[i] < tailTable[0]:
            tailTable[0] = nums[i]
        elif nums[i] > tailTable[k-1]:
            tailTable[k] = nums[i]
            k+=1
        else:
            idx = bisect_right(tailTable, nums[i], 0, k-1)
            if idx != 0 and tailTable[idx -1 ] == nums[i]:
                continue
            # print('idx: {}'.format(idx))
            tailTable[idx] = nums[i]
    return k >= 3



def increasingTripletOrderOneSpaceSolution(nums: List[int]) -> bool:

    n = len(nums)
    if n == 0:
        return False
    first = second = float("inf")
    # store lowest two numbers, if greater than that found, return True else return False
    for i in nums:
        if i <= first:
            first = i
        elif i <= second:
            second = i
        else:
            return True
    return False



nums = [1,2,3]
nums = [2, 5, 3, 7, 11, 8, 10, 13, 6 ]
nums = [1,2,1,2,1,2,1,2,1,2]
nums = [3, 2, 1]
# nums = [2,1,5,0,4,6]
# nums = [5, 2, 1, 6, 7]
nums = [5, 10, 3, 2, 20]
print(increasingTriplet(nums))
print(increasingTripletOrderOneSpaceSolution(nums))




