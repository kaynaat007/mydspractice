"""
Consider the edge cases.

This implementation of binary search gives leftmost index of target in array
if target is not there, it returns -1
Ofcourse this implementation has an array in which each element is a two element long.
"""

from typing import List


def b_search(arr, low, high, target, n):

    if low > high:
        return -1

    mid = low + (high - low) // 2
    u, v, _ = arr[mid]

    if u >= target:
        if mid == low:
            return mid
        else:
            prev_u, prev_v, _ = arr[mid-1]
            if prev_u < target:
                return mid
            else:
                return b_search(arr, low, mid-1, target, n)
    else:
        return b_search(arr, mid + 1, high, target, n)


def findRightInterval(intervals: List[List[int]]) -> List[int]:

    order = []
    for i, e in enumerate(intervals):
        u, v = e
        order.append(u)
        e.append(i)

    intervals = sorted(intervals, key=lambda x: x[0])
    output = {}
    n = len(intervals)
    for i, e in enumerate(intervals):
        u, v, _ = e
        idx = b_search(intervals, i, n-1, v, n)
        if idx != -1:
            _, _, original_index = intervals[idx]
            output[u] = original_index
        else:
            output[u] = -1

    return [output[u] for u in order]


intervals = [[1, 2]]
intervals = [[1, 2], [2, 3]]
# intervals = [[3,4],[2,3],[1,2]]
# intervals = [[1,4],[2,3],[3,4]]
# intervals = [[3, 8], [1, 2], [4, 5]]

# intervals = [[1,1],[3,4]]

# intervals = [[1, 1]]

print(findRightInterval(intervals))



