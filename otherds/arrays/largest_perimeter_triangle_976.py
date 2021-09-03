"""
simple problem based on triangle property a + b  > c 
"""
from typing import List


def largestPerimeter(A: List[int]) -> int:

    A = sorted(A, reverse=True)
    print(A)
    n = len(A)
    for i in range(n-2):
        if A[i] + A[i+1] > A[i+2] and A[i] + A[i+2] > A[i+1] and A[i+1] + A[i+2] > A[i]:
            return A[i] + A[i+1] + A[i+2]
    return 0

a = [2, 1, 2]
a = [1, 2, 1]
a = [3, 2, 3, 4]
a = [3, 6, 2, 3]
print(largestPerimeter(a))
