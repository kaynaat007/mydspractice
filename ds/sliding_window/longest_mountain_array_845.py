""""
approach 1. Time O(n), space: O(n)
---------

"""


def longestMountainUtil(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    n = len(arr)
    left_to_right = [1] * n
    right_to_array = [1] * n
    max_len = 0

    for i in range(1, n):
        if arr[i] > arr[i-1]:
            left_to_right[i] += left_to_right[i-1]

    for i in range(n-1, 0, -1):  # 0,1,2,3,4,5
        if arr[i-1] > arr[i]:
            right_to_array[i-1] += right_to_array[i]

    for k in range(n):
        x = left_to_right[k]
        y = right_to_array[k]
        if x > 1 and y > 1:
            max_len = max(max_len, x + y - 1)

    if max_len < 3:
        return 0
    return max_len

def longestMountainUtilSlidingWindow(arr):
    """
    todo: This can also be done by sliding window  by taking two pointers
    :type arr: List[int]
    :rtype: int
    """



arr=[2,1,4,7,3,2,5]
arr = [2,2,2]
arr = [1,2,3,2,1,5,6,7,8,1]
print(longestMountainUtil(arr))




