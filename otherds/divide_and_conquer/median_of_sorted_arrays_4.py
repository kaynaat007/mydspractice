from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:

    n1 = len(nums1)
    n2 = len(nums2)
    if n1 == 0 and n2 == 0:
        return 0.0

    result = [0 for _ in range(n1 + n2)]
    i = 0
    j = 0
    k = 0
    while i < n1 and j < n2:

        if nums1[i] < nums2[j]:
            result[k] = nums1[i]
            i += 1
        else:
            result[k] = nums2[j]
            j += 1

        k += 1

    while i < n1:
        result[k] = nums1[i]
        i += 1
        k += 1
    while j < n2:
        result[k] = nums2[j]
        j += 1
        k += 1

    mid = k // 2
    if k % 2 == 0:
        return (result[mid] + result[mid-1])/2
    return result[mid]


num1 = [2]
num2 = [5]

num1 = [2]
num2 = []

num1 = []
num2 = [1]

num1 = [0, 0]
num2 = [0, 0]

num1 = [1, 2]
num2 = [3, 4]

num1 = [1, 3]
num2 = [2]

num1 = [5, 6]
num2 = [5, 6, 7]
print(findMedianSortedArrays(num1, num2))






