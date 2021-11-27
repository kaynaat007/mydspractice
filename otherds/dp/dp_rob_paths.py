"""
Circular version of Max non adjacent sum

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount
of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.

let NAMS = Non adjacent max sum

We need to chose houses which are non adjacent. A dp solution exists for a non adjacent max sum
we leverage that try to find max of two quantities:
    NAMS for array including the first element and excluding last element
    NAMS for arrat excluding first element and including last element.

We do that since first and last element are connected as list is circular.

NAMS:
  if we know two peices of information of elements of A at index i-1,
     1. maximum NAMS till element i-1 including it.
     2. maximum NAMS till element i-1 exluding it.

  Then we can calculate NAMS at index i as follows:

    1. NAMS at index i including element i will be max of previous excl[i-1] + A[i] and A[i]
    2. NAMS at index i exluding element i will be max of exl[i-1], incl[i-1]

"""

def max_non_adjacent_sum(A):

    n = len(A)
    inc = [0 for _ in range(n)]
    exl = [0 for _ in range(n)]

    inc[0] = A[0]
    exl[0] = 0

    for i in range(1, n):
        exl[i] = max(inc[i-1], exl[i-1])
        inc[i] = max(exl[i-1] + A[i], A[i])

    # print("excl array", exl)
    # print("incl array", inc)
    return max(max(exl), max(inc))


def main(A):
    n = len(A)
    if n == 0:
        return 0
    if n == 1:
        return A[0]
    s1 = max_non_adjacent_sum(A[1:])
    s2 = max_non_adjacent_sum(A[:n-1])
    print(max(s1, s2))

A = [1, 2]
# A = [1,2,3,1]
# A = [2,1,1,2, 5]
# A = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# A = [2, 4, 1]
# print(rob(A))
main(A)