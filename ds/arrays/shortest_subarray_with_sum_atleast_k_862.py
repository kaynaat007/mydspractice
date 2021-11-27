"""
Status: Unsolved


"""
import math
from typing import List

def b_search(arr, low, high, right, target, n):

    if low > high:
        return -1

    mid = low + (high - low) // 2

    if arr[right] - arr[mid-1] >= target:
        if arr[right] - arr[mid] < target:
            return mid
        elif arr[right] - arr[mid] >= target:
            return b_search(arr, mid + 1, high, right, target, n)
    else:
        return b_search(arr, low, mid-1, right,  target, n)


def minimum_size_subarray_sum(target, nums):

    n = len(nums)
    prefix = [0 for _ in range(n+1)]
    prefix[1] = nums[0]
    for i in range(2, n+1):
        prefix[i] = prefix[i-1] + nums[i-1]

    # print('prefix array: {}'.format(prefix))

    min_length = math.inf

    for k in range(n, 0, -1):
        index = b_search(prefix, 1, k, k, target, n)
        if index == -1:
            continue
        min_length = min(min_length, k - index + 1)
    if min_length == math.inf:
        return -1
    return min_length


def shortestSubarray(A: List[int], K: int) -> int:

    min_number = min(A)
    if min_number >= 0:
        return minimum_size_subarray_sum(K, A)
    else:
        min_number = -1 * min_number
        n = len(A)
        for i in range(n):
            A[i] = A[i] + min_number
        K = K + n * min_number
        print(A, K)
        return minimum_size_subarray_sum(K, A)

A = [2, -1, 2]
K = 3

A = [-10]
K = 10

A = [1, 2]
K = 4

A = [48,99,37,4,-31]
K = 140

print(shortestSubarray(A, K))
