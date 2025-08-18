from typing import List


def findFinalValue(nums: List[int], original: int) -> int:
    into_set = set(nums)
    while original in into_set:
        original = original * 2
    return original


n = [5, 3, 6, 1, 12]
o = 3
print(findFinalValue(n, o))

