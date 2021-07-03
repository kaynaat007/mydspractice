"""
Two sum problem solution should give motivation for this.
Given a sorted array , find all pairs which sum to T
keep a hash of elements with their frequency in a dict

[1, 1, 1, 1, 2, 8, 8, 8 ]

8 -- 3
2 -- 1
1 ---4

if T is 9
take 1 --- find T - 1 = 8 check freq of 8 = 3 add 3 to ans.
take second 1 -- find T - 1 = 8, check freq of 8 = 3 add 3 to ans.

similary.
There is relation here between frequency and pair sum.
Same approach has been extended here to find the count.

"""


from typing import List
from collections import defaultdict, Counter


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.freq = defaultdict(int)
        self.freq = Counter(nums2)
        self.nums1 = nums1
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        """
        O(1)
        """
        self.freq[self.nums2[index]] -= 1

        self.nums2[index] += val

        self.freq[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        """
        O(n) time
        """
        pairs_count = 0
        for e in self.nums1:
            pairs_count += self.freq[tot-e]
        return pairs_count


nums1 = [1, 1, 2, 2, 2, 3]
nums2 = [1, 4, 5, 2, 5, 4]
c = FindSumPairs(nums1, nums2)
print(c.count(7))
c.add(3, 2)
print(c.count(8))



