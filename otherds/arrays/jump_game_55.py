from typing import List


def canJump(nums: List[int]) -> bool:
    step = nums[0]
    max_ladder = nums[0]
    i = 0
    n = len(nums)
    if n == 1:
        return True
    while step > 0 and i < n:
        max_ladder = max(max_ladder, i + nums[i])
        step -= 1
        if step == 0:
            step = max_ladder - i
        if step == 0:
            break
        i += 1
    if i >= n-1:
        return True
    return False


nums = [3,2,1,0,4]
nums = [2, 3, 4, 5]
nums = [0]
nums = [2, 0, 0, 0]
nums = [1, 0, 2, 3]
print(canJump(nums))