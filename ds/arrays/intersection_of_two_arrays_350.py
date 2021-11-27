from typing import List
from collections import Counter


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:

    hash1 = Counter(nums1)
    hash2 = Counter(nums2)
    commons = set()
    ans = []
    for key, count in hash2.items():
        if key in hash1:
            commons.add(key)
            hash1[key] = min(hash1[key], count)

    for e in commons:
        count = hash1[e]
        while count > 0:
            ans.append(e)
            count -= 1
    return ans


nums1 = [1,2,2,1]
nums2 = [2, 2]

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]


print(intersect(nums1, nums2))



