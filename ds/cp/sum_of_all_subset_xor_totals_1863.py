from typing import List


def util(arr, i, n):
    if i == n:
        return [[]]
    result = []
    subsets = util(arr, i+1, n)
    for subset in subsets:
        subset_copy = subset.copy()
        subset_copy.append(arr[i])
        result.append(subset)
        result.append(subset_copy)
    return result


def subsetXORSum(nums: List[int]) -> int:
    i = 0
    n = len(nums)
    subsets = util(nums, i, n)
    ans = 0

    for subset in subsets:
        xor_sum = 0
        for item in subset:
            xor_sum = xor_sum ^ item
        ans += xor_sum
    return ans


nums = [1, 3]
nums = [5,1,6]
nums = [3,4,5,6,7,8]
print(subsetXORSum(nums))



