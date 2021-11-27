from typing import List


def two_sum_util(arr, target, i, j):

    while i < j:
        curr_sum = arr[i][1] + arr[j][1]
        if curr_sum < target:
            i += 1
        elif curr_sum > target:
            j -= 1
        else:
            return [arr[i][0], arr[j][0]]
    return []


def twoSum(nums: List[int], target: int) -> List[int]:

    return two_sum_util_using_dict(nums, target)


def two_sum_util_using_dict(arr, target):

    store = {}
    for i , e in enumerate(arr):
        if e not in store:
            store[e] = i

    for i, e in enumerate(arr):
        t = target - e
        if t in store and store[t] != i:
            return [i, store[t]]



nums = [2,7,11,15]
target = 9

nums = [3,2,4]
target = 6


#
nums = [3,3]
target = 6



print(twoSum(nums, target))


