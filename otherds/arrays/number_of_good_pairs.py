from typing import List
from collections import defaultdict


def numIdenticalPairs(nums: List[int]) -> int:
    hash = defaultdict(int)
    for e in nums:
        hash[e] += 1
    ans = 0
    for key, count in hash.items():
        v = (count * count - count)//2
        ans += v
    return ans


nums = [1,1,1]
nums = [1,2,3,1,1,3]
nums = [1,1,1,1]
nums = [1,2,3]
print(numIdenticalPairs(nums))

