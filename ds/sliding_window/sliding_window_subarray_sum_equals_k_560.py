"""
Cannot be solved via two pointer technique.

why ?


Need hash to store prefix sum aas key and value as count of that sum ( to handle multiple same prefixes occurring )

idea is to have a running sum till index i so far say X.
At each index, increase X and
look for X - T in hash, T being target sum.
if you found it this means, array starting from 1 index more than whatever index X - T was till current index
must sum up to T since (X - T)[was found in has]  + T ( our target ) = X [ current sum ]

"""
from collections import defaultdict

def subarray_sum_equals_k(a, k):
    curr_sum = 0
    n = len(a)
    prefix_map = defaultdict(lambda : 0)
    count = 0
    for i in range(n):
        curr_sum += a[i]
        if curr_sum == k:
            count += 1
        remaining_sum = curr_sum - k
        if remaining_sum in prefix_map:
            count += prefix_map[remaining_sum]
        prefix_map[curr_sum]+= 1
    return count


a = [1, 1, 1]
a = [-1, -1, -1, -1]
a = [1, -2, -4, 3]
a = [0, 0, 0]
a = [0,0,0,0,0,0,0,0,0,0]
a = [5, 0, -2, -3]

# a = [2, 0, 2]
# k = -4 + 3
# a = [3, 4, 1, 2, 3, 4, 5]
k = -5
print(subarray_sum_equals_k(a, k))
