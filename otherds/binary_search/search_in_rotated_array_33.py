from typing import List


def search(nums: List[int], target: int) -> int:
    """
    nums is rotated.
    general case is when no duplicates:
        check of left half is sorted:
            check if target can lie in left half ==> update high
            else:
            update low
        else right half must be sorted:
            check if target can lie in right half == update low
            else:
                update high
    for duplicates processing,
    check if arr[low] == arr[mid] == arr[high]
        low += 1
        high -= 1
    """
    n = len(nums)
    if n == 1:
        if nums[0] == target:
            return 0
        else:
            return -1
    if n == 2:
        if nums[0] == target:
            return 0
        elif nums[1] == target:
            return 1
        else:
            return -1
    low = 0
    high = n-1
    while low <= high:

        mid = low + (high - low) // 2

        if high - low + 1 == 2:
            if nums[low] == target:
                return low
            if nums[low + 1] == target:
                return low + 1
        # print('low: {}, high: {}, mid: {}'.format(low, high, mid))
        if nums[mid] == target:
            return mid

        if nums[low] < nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1

nums = [5, 1, 2, 3, 4]
target = 4

#
# nums = [4,5,6,7,0,1,2]
# target = 0

# nums = [4,5,6,7,0,1,2]
# target = 3


# nums = [4,5, 6,7,8,9, 10, 0,1,2]
# target = 9

nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1] # duplicates case
target = 2

# nums = [5, 5, 5, 5, 1, 2, 3, 3, 3, 3]
# target = 2


nums = [2,2,2,0,0,1]
target = 0

print(search(nums, target))

