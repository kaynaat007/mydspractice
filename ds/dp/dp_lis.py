"""

optimal substructure:

assume we know lis of all indexes from 0 to j before we calculate lis at index i.
lis at index i needs that all sub-problems are themselves lis at their respective indexes because if they are not,
we can't say that lis at i has any relationship to the subproblems at all other indexes j < i.
so solution to a bigger problem ( at index i ) depends on solution to smaller problems ( at indexes j < i ).

recursive formulation to calculate optimal value:

let lis[i] represent optimal value at index i. Assume we knoe lis at all indexes j < i. Then

lis[i] = 1 for all i initially since individual elements are single element LIS.

lis[i] will be max (1 + lis[j], lis[i]) if arr[j] < arr[i] for  0<=j < i.

compute the optimal value ( TD/BU):

we take bottom up approach. maintain an array LIS[n].

LIS[i] will be length of longest increasing subsequence of array A ending at index i.

LIS[i] = 1 for  0<=i <=n-1

Then we look at all indexes j < i and calculate LIS[i] by the above recursion formula.


"""

from datetime import datetime

def lis(x):
    n = len(x)
    lis = [0 for i in range(n)]
    for i in range(0, n):
        lis[i] = 1
        for j in range(0, i):
            if x[j] < x[i]:
                lis[i] = max(lis[i], 1 + lis[j])
    return lis


# Python program to find
# length of longest
# increasing subsequence
# in O(n Log n) time

# Binary search (note
# boundaries in the caller)
# A[] is ceilIndex
# in the caller
def CeilIndex(A, l, r, key):
    while (r - l > 1):

        m = l + (r - l) // 2
        if (A[m] >= key):
            r = m
        else:
            l = m
    return r


def LongestIncreasingSubsequenceLengthNLOGN(A, size):
    # Add boundary case,
    # when array size is one

    tailTable = [0 for i in range(size + 1)]
    len = 0  # always points empty slot

    tailTable[0] = A[0]
    len = 1
    for i in range(1, size):

        print(tailTable)

        if (A[i] < tailTable[0]):

            # new smallest value
            tailTable[0] = A[i]

        elif (A[i] > tailTable[len - 1]):

            # A[i] wants to extend
            # largest subsequence
            tailTable[len] = A[i]
            len += 1

        else:
            # A[i] wants to be current
            # end candidate of an existing
            # subsequence. It will replace
            # ceil value in tailTable
            idx = CeilIndex(tailTable, -1, len - 1, A[i])
            print('idx: {}'.format(idx))
            tailTable[idx] = A[i]

    return len


# Driver program to
# test above function

A = [2, 5, 3, 7, 11, 8, 10, 13, 6]
A = [1,2,1,2,1,2,1,2,1,2]
n = len(A)

print("Length of Longest Increasing Subsequence is ",
      LongestIncreasingSubsequenceLengthNLOGN(A, n))


# x = [1,2,3]
# x = [10,9,2,5,3,7,101,18]
# x = [10, 22, 9, 33, 21, 50, 41, 60, 80]
# x = [1,3,6,7,9,4,10,5,6]
# t = datetime.now()
# print(lis(x))
# print((datetime.now() - t).total_seconds() * 1000)
