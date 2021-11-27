"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.


Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.


Do not memorise it.
Solution can come naturally if you can remember basic properties of multiplication

a negative number  * a negative number ==> a positive number
a negative number * positive == negative
positive * positive == positive
Remember that

Also define two arrays where

positive_product[i] means maximum positive product including the element A[i] at i.
negative_product[i] means maximum absolute negative product including A[i] at i.

say you have these value till i-1

question is how to extend it to ith element.

Two possibilities at i:

Either ith element can kickstart a completely new subarray starting at i.
OR
it can be multiplied to one of these array elements at i-1 index and get a new value at i which is more optimal.

depends on where ith element can contribute.

if A[i] is negative,

    then multiplying by max negative prod at i - 1 , A[i] can contribute towards a larger positive
    product.

    if negative i - 1 is not present however, then A[i] is new start of subarray at position i

if A[i] is positive,

    we can get more negative prod at i by multiplying a negative prod at i - 1 by A[i]
    if negative prod at i -1 is not present, then A[i] can start a new prod subarray at position i.



"""

def max_prod_subarray(A):
    """

    """
    n = len(A)
    negative_product = [None for _ in range(n)]
    positive_product = [None for _ in range(n)]

    if A[0] >= 0:
        positive_product[0] = A[0]
    else:
        negative_product[0] = A[0]

    for i in range(1, n):

        if A[i] >= 0:

            positive_product[i] = A[i]

            if positive_product[i-1]:
                positive_product[i] = positive_product[i - 1] * A[i]

            if negative_product[i-1]:
                negative_product[i] = negative_product[i-1] * A[i]

        if A[i] < 0:

            negative_product[i] = A[i]

            if negative_product[i-1]:
                positive_product[i] = negative_product[i-1] * A[i]

            if positive_product[i-1]:
                negative_product[i] = positive_product[i-1]  * A[i]

    max_prod_not_none_arrray = list(filter(lambda x: x is not None, positive_product))
    max_prod_neg_not_none_array = list(filter(lambda x: x is not None, negative_product))
    if max_prod_not_none_arrray:
        max_prod = max(max_prod_not_none_arrray)
        return max_prod
    else:
        max_neg_prod = min(max_prod_neg_not_none_array)
        return max_neg_prod


from typing import List


def max_prod_subarray_practice_1(nums: List[int]):

        n = len(nums)
        if n == 0:
            return 0
        P = [-1 for _ in range(n)]
        N = [0 for _ in range(n)]

        for i in range(n):

            if nums[i] == 0:
                P[i] = 0
                N[i] = 0

            if nums[i] > 0:

                if i -1 >= 0 and P[i-1] != -1:
                    P[i] = max(nums[i], P[i-1] * nums[i])
                else:
                    P[i] = nums[i]

                if N[i-1] < 0 <= i - 1:
                    N[i] = N[i-1] * nums[i]

            if nums[i] < 0:

                if P[i-1] > 0:
                    N[i] = min(nums[i],P[i-1] * nums[i])
                else:
                    N[i] = nums[i]
                if N[i-1] < 0 <= i-1:
                    P[i] = N[i-1] * nums[i]

        ans = max(P)
        if ans == -1:
            return max(N)
        return max(P)





A = [-10, -2, 3]
A = [1, 2, 3]
# A = [-1,  -3, -2, 4, -2, 4]
# A = [-1, -3, -2, 4, -2]
# A = [1, 3, -4, -2, 4]
# A = [-2,0,-1]
# A = [0, 1, 0, 2]
# A = [-100, -200, -300]
A = [-1, 100]
print(max_prod_subarray(A))
print(max_prod_subarray_practice_1(A))