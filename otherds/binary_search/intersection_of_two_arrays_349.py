from typing import List
from bisect import bisect_left


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:

    n = len(nums1)
    m = len(nums2)
    if n == 0 or m == 0:
        return []
    output = set()
    if n <= m:
        array1 = nums1
        array2 = nums2
    else:
        array1 = nums2
        array2 = nums1

    array2 = sorted(array2)
    m = len(array2)
    for e in array1:
        idx = bisect_left(array2, e)
        if idx < m and array2[idx] == e:
             output.add(e)
    return list(output)


nums1 = [1, 2]
nums2 = [2, 2]

nums1 = [1,2,2,1]
nums2 = [2,2]

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

nums1 = []
nums2 = [3, 3, 4]

print(intersection(nums1, nums2))




