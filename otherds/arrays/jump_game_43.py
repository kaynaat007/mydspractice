from typing import List


def jump(nums: List[int]) -> int:

    max_ladder = nums[0]
    steps = nums[0]
    j = 1
    n = len(nums)
    if n == 1:
        return 0
    jumps = 1
    while j < n:
        current_ladder = nums[j] + j
        max_ladder = max(max_ladder, current_ladder)
        steps -= 1
        if steps == 0:
            if j < n-1:
                jumps += 1
            steps = max_ladder - j
        j += 1


    return jumps


# nums = [4, 0, 0, 0, 1, 5]

nums = [2,3,1,1,4]
nums = [2,3,0,1,4]
print(jump(nums))

