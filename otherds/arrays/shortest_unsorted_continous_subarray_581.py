from typing import List


def swap(nums, i, j):
    t = nums[i]
    nums[j] = nums[i]
    nums[i] = t

def findUnsortedSubarray(nums: List[int]) -> int:

    c = 0
    low = 0
    high = 0
    n = len(nums)
    for i in range(n):
        if nums[i] > nums[i+1]:
            swap(nums, i, i+1)
            low = i
            high = i+1




