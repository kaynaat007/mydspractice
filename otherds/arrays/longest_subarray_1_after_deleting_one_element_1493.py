from typing import List


def longestSubarray(nums: List[int]) -> int:

    lengths = []
    n = len(nums)
    i = 0
    length = 0
    while i < n:
        if nums[i] == 0:
            lengths.append(length)
            length = 0
            i += 1
            continue
        length += 1
        i += 1

    if length != 0:
        lengths.append(length)

    if len(lengths) == 1:
        return lengths[0] - 1

    i = 0
    max_len = 0
    while i + 1 < len(lengths):
        if lengths[i] + lengths[i+1] > max_len:
            max_len = lengths[i] + lengths[i+1]
        i += 1

    return max_len


nums = [1, 0, 0]
# nums = [1,1,0,1]
# nums = [0,1,1,1,0,1,1,0,1]
# nums = [1,1,1]
# nums = [1,1,0,0,1,1,1,0,1]
# nums = [0, 0, 0]
nums = [0, 1, 1, 1, 0, 1, 0 ,0 , 0, 1,1,1,1,1,1,1,1,1]
print(longestSubarray(nums))

