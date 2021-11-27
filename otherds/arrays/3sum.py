from typing import List


def twoSum(nums, i, j, target):

    ans = []
    left = None
    right = None
    while i < j:
        curr_sum = nums[i] + nums[j]
        if curr_sum == target:
            if left is not None and right is not None and nums[i] == left and nums[j] == right:
                i = i + 1
                j = j - 1
                continue
            ans.append([nums[i], nums[j]])
            left = nums[i]
            right = nums[j]
            i = i + 1
            j = j - 1
            continue
        if curr_sum > target:
            j = j - 1
        else:
            i = i + 1
    return ans


def threeSum(nums: List[int]):

    nums = sorted(nums)
    output = []
    n = len(nums)
    prev = None
    for i, e in enumerate(nums):
        if (prev is not None) and prev == e:
            continue
        else:
            prev = e
        ans = twoSum(nums, i+1, n-1, -1 * e)
        for first, second in ans:
            output.append([e, first, second])
    return output


nums = [1, 1, 2, 3, 4, 4, 6, 7, 7, 10, 12]
# nums =  [-1,0,1,2,-1,-4]

# nums = []
# nums = [0]
# nums = [0,0,0]
# nums = [-2,0,0,2,2]
print(threeSum(nums))