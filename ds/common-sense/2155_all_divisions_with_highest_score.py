'''
complexity :  O(n) + O(n) +  nO(logn)
'''
from typing import List
import heapq


def prepare_left_right(nums):
    n = len(nums)
    left_right_sum = [0 for _ in range(n)]
    if nums[0] == 0:
        left_right_sum[0] = 1
    for i, e in enumerate(nums):
        if i > 0:
            if nums[i] == 0:
                left_right_sum[i] = left_right_sum[i - 1] + 1
            else:
                left_right_sum[i] = left_right_sum[i - 1]
    return left_right_sum


def prepare_right_left(nums):
    n = len(nums)
    right_left_sum = [0 for _ in range(n)]
    if nums[-1] == 1:
        right_left_sum[-1] = 1
    for i in range(n-1, -1, -1):
        if i < n-1:
            if nums[i] == 1:
                right_left_sum[i] = right_left_sum[i + 1] + 1
            else:
                right_left_sum[i] = right_left_sum[i + 1]
    return right_left_sum


def maxScoreIndicesUtil(nums: List[int]) -> List[int]:
    n = len(nums)
    left_sum = prepare_left_right(nums)
    right_sum = prepare_right_left(nums)
    indices = []
    output = set()
    for i in range(n+1):
        if i == 0:
            left_score = 0
            right_score = right_sum[i]
        elif i == n:
            left_score = left_sum[i-1]
            right_score = 0
        else:
            left_score = left_sum[i-1]
            right_score = right_sum[i]
        score = left_score + right_score
        heapq.heappush(indices, (-1 * score, i))
    prev_score = None
    while indices:
        score_, index = heapq.heappop(indices)
        if prev_score is None:
            output.add(index)
        elif prev_score is not None and score_ == prev_score:
            output.add(index)
        else:
            break
        prev_score = score_
    return list(output)



nums = [0, 0, 1, 0]
nums = [0, 0, 0]
nums = [1, 1]
nums = [1, 1, 0, 0]
print(maxScoreIndicesUtil(nums))


