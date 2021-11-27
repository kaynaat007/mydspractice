from typing import List


def two_sum(arr, target, i, j):
    output = []
    while i < j:
        curr_sum = arr[i] + arr[j]
        if curr_sum < target:
            i += 1
        elif curr_sum > target:
            j -= 1
        else:
            output.append((i, j))
            i += 1
            j -= 1
    return output


def fourSum(nums: List[int], target: int):

    result = set()
    nums = sorted(nums)
    n = len(nums)

    for i in range(n-3):
        for j in range(i+1, n-2):
            remaining_sum = target - (nums[i] + nums[j])
            remaining_indexes = two_sum(nums, remaining_sum, j+1, n-1)
            for a, b in remaining_indexes:
                if a is not None and b is not None:
                    result.add((nums[i], nums[j], nums[a], nums[b]))

    result = [list(content) for content in result]
    return result


nums = [1, 2, 0, 1] # [0, 1, 1, 2]
target = 4
#
nums = [1,0,-1,0,-2,2] # [ -2, -1, 0, 0,
target = 0

# nums = []
# target = 0


nums = [-3,-1,0,2,4,5] # 5 + -3 = 2, T = 0 - 2 = -2,
target = 0


nums = [-2,-1,-1,1,1,2,2]
target = 0

nums = [-3,-1,0,2,4,5]
target = 2

print(fourSum(nums, target))


