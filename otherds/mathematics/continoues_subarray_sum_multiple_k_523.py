"""

if S[i] represents sum of numbers till index  i,
then S[j] - S[i-1] = sum of numbers from index i to index j
This sum is n * k where k is given and n is an integer

S[j] - S[i-1] = n * k
S[j] = S[i-1] + n * k
S[j] mod k = S[i-1] mod k + (n * k) mod k
S[j] mod k = S[i-1] mod k + 0
S[j] and S[i-1] are congruent equal modulo k meaning if we divide S[j] and S[i-1] by k and get the remainder,
remainder will be same.

so if we ecounter S[i-1] and then after atleast 2 elements, we encounter S[j],  and they both have same remainder
then we can say S[j] - S[i-1] = n * k

corner case

check if input array has atleast two consecutive zeroes. return True
if  k == 0 and array does not has two consecutive zeroes, return False.
if k is negative
normal case

"""

from typing import List

def checkSubarraySum(nums: List[int], k: int) -> bool:
    """
    """
    n = len(nums)
    if n < 2:
        return False

    for i in range(n-1):
        if nums[i] == 0 and nums[i+1] == 0:
            return True
    if k == 0:
        return False

    k = abs(k)

    prefix = {0: -1}
    s = 0
    for i in range(n):
        print(prefix)
        s = s + nums[i]
        r = s % k
        if r in prefix and (i - prefix[r] + 1 >= 3):
            return True
        if r not in prefix:
            prefix[r] = i
    return False



nums = [23, 2, 4, 6, 7]
k =  6

nums = [1, 10,  20]
k = 0

nums = [23, 2, 6, 4, 7]
k = 6

nums = [1, 2]
k = 2

nums = [0, 1, 0]
k = -1
print(checkSubarraySum(nums, k))




