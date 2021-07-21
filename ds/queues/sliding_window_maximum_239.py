"""
uses Monotonic dequeue
maintains a decreasing dequeue of elements while scanning from left to right
"""

from typing import List
from collections import deque


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:

    max_q = deque([])
    n = len(nums)
    output = []

    if n == 0:
        return []

    for i in range(k):
        if not max_q:
            max_q.append(nums[i])
        else:
            if nums[i] < max_q[-1]:
                max_q.append(nums[i])
            else:
                while max_q and nums[i] > max_q[-1]:
                    max_q.pop()
                max_q.append(nums[i])
    print(max_q)
    i = 0
    j = k
    output.append(max_q[0])
    while j < n:

        while max_q and nums[j] > max_q[-1]:
            max_q.pop()
        max_q.append(nums[j])
        if max_q and nums[i] == max_q[0]:
            max_q.popleft()
        output.append(max_q[0])
        j += 1
        i += 1
    return output


arr = [1,3,-1,-3,5,3,6,7]
k = 3

arr = [9, 11]
k = 2

arr = [4, -2]
k = 2

arr = [1]
k = 1

arr = [7, 9, 5, 4, 3, 1]
k = 3

arr = [9,10,9,-7,-4,-8,2,-6]
k = 5
print(maxSlidingWindow(arr, k))








