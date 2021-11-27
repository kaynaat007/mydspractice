from typing import List


def b_search(arr, low, high, target, n, left):

    if low < 0:
        return -1
    if high > n:
        return -1
    if high < low:
        return -1
    mid = low + (high - low)//2
    if arr[mid] == target:
        if left:
            left = mid
            left_r = b_search(arr, low, mid-1, target, n, left)
            return left if left_r == -1 else left_r
        else:
            right = mid
            right_r = b_search(arr, mid+1, high, target, n, left)
            return right if right_r == -1 else right_r
    elif target < arr[mid]:
        return b_search(arr, low, mid-1, target, n, left)
    return b_search(arr, mid + 1, high, target, n, left)


def searchRange(nums: List[int], target: int) -> List[int]:

     v1 = b_search(nums, 0, len(nums)-1, target, len(nums), True)
     v2 =  b_search(nums, 0, len(nums)-1, target, len(nums), False)
     return [v1, v2]

nums = [4, 4, 6, 6, 6, 8, 10, 10]
target = 4

nums = [5,7,7,8,8,10]
target = 10

nums = []
target = 0

print(searchRange(nums, target))
