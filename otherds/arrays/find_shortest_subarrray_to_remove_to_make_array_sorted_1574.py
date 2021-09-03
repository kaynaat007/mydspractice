from typing import List
import math


def findLengthOfShortestSubarray(arr: List[int]) -> int:
    """
    struggled
    3 cases
        remove a prefix
        remove a sufix
        or remove some middle part
    """
    remove_from_middle_length = math.inf
    n = len(arr)
    if n == 1:
        return 0

    prev = 0
    i = 1
    while i < n and arr[prev] <= arr[i]:
        prev = i
        i += 1

    start = i - 1

    remove_suffix_length = n - i

    prev = n-1
    i = n-2
    while i >= 0 and arr[i] <= arr[prev]:
        prev = i
        i -= 1
    remove_prefix_length = prev
    end = prev

    if start == n-1:
        return 0

    # print('start: {}, end: {}'.format(start, end))

    i = 0  # take start of left increasing array
    j = end  # take start of right increasing array

    while i <= start and j < n:
        if arr[i] <= arr[j]:
            remove_from_middle_length = min(remove_from_middle_length, j - i - 1)
            i += 1  # shrink
        else:
            j += 1  # expand

    # print(remove_suffix_length, remove_prefix_length, remove_from_middle_length)
    return min(remove_prefix_length, remove_suffix_length, remove_from_middle_length)




def findLengthOfShortestSubarrayV2(arr: List[int]) -> int:
    """
    struggled
    3 cases
        remove a prefix
        remove a sufix
        or remove some middle part

    we just change two different ends
    """
    remove_from_middle_length = math.inf
    n = len(arr)
    if n == 1:
        return 0

    prev = 0
    i = 1
    while i < n and arr[prev] <= arr[i]:
        prev = i
        i += 1

    start = i - 1

    remove_suffix_length = n - i

    prev = n-1
    i = n-2
    while i >= 0 and arr[i] <= arr[prev]:
        prev = i
        i -= 1
    remove_prefix_length = prev
    end = prev

    if start == n-1:
        return 0

    # print('start: {}, end: {}'.format(start, end))

    i = start # take end of left increasing array
    j = n-1  # take end of right increasing array

    while i >= 0 and j >= end:

        if arr[i] <= arr[j]:
            remove_from_middle_length = min(remove_from_middle_length, j - i - 1)
            j -= 1  # shrink
        else:
            i -= 1  # expand

    # print(remove_suffix_length, remove_prefix_length, remove_from_middle_length)
    return min(remove_prefix_length, remove_suffix_length, remove_from_middle_length)


def get_left_index(arr, low, high, target):

    if low > high:
        return high + 1
    mid = low  + (high - low) // 2

    if mid == 0 and arr[mid] == target:
        return mid
    elif arr[mid-1] != target and arr[mid] == target:
        return mid
    elif arr[mid-1] == target and arr[mid] == target:
        return get_left_index(arr, low, mid-1, target)
    elif target < arr[mid]:
        return get_left_index(arr, low, mid-1, target)
    else:
        return get_left_index(arr, mid+1, high, target)


def findLengthOfShortestSubarraybinarySearch(arr: List[int]) -> int:
    """
    struggled
    3 cases
        remove a prefix
        remove a sufix
        or remove some middle part

    we just change two different ends
    """
    remove_from_middle_length = math.inf
    n = len(arr)
    if n == 1:
        return 0

    prev = 0
    i = 1
    while i < n and arr[prev] <= arr[i]:
        prev = i
        i += 1

    start = i - 1

    remove_suffix_length = n - i

    prev = n-1
    i = n-2
    while i >= 0 and arr[i] <= arr[prev]:
        prev = i
        i -= 1
    remove_prefix_length = prev
    end = prev

    if start == n-1:
        return 0

    for i in range(start + 1):
        left_most_index = get_left_index(arr, end, n-1, arr[i])
        # print('left most idex: {}'.format(left_most_index))
        if i < left_most_index:
            remove_from_middle_length = min(remove_from_middle_length, left_most_index - i - 1)

    return min(remove_prefix_length, remove_suffix_length, remove_from_middle_length)


arr = [5, 6, 3, 6, 10, 9, 8]

# arr =  [5, 6, 7, 20, 19, 16, 18, 19, 10, 9, 20, 21, 100, 40, 100]
# arr = [5, 6, 7, 20, 20, 20, 19, 16, 18, 19, 10, 9, 20, 21, 100, 40, 100]
arr = [1,2,3,10,4,2,3,5]

# arr = [3, 2, 1]
# arr = [1,2,3]
# arr = [100, 100, 100]
arr = [45, 90, 23, 12, 6, 9, 100]
# arr = [3, 100, 78, 21, 34, 11]
# arr = [2,2,2,1,1,1]
# arr = [5, 4, 3, 2, 1]
# arr = [1,2,2,2,2,2,3,1,7,5,1,2,2,2,2,2,2,5,6]
# arr = [13,0,14,7,18,18,18,16,8,15,20]
# arr = [1, 2, 3]
# arr = [1]
# arr = [1, 2, 3, 2, 6, 8, 30, 15, 20, 30, 40, 60]
# arr = [6,3,10,11,15,20,13,3,18,12]
# arr = [11,26,3,14,24,6,10,16,32,9,36,24,27,17,31,32,35,36,11,22,30]
# arr = [13,0,14,7,18,18,18,16,8,15,20]

print(findLengthOfShortestSubarray(arr))
print(findLengthOfShortestSubarraybinarySearch(arr))



