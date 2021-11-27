"""
Adapted from Longest increasing subsequence.

O(n^2)

Let L[i] be length of longest wiggle subsequence ending at i.
for all j < i we can add 1 to L[j]

    if nums[j] was less tha prev element in subsequence and nums[j] > nums[i].
    if nums[j] was more than prev element in subsequence and nums[j] < nums[i]

to save that a given number in subsequence was less than or more than prev element in the same subsequence ,
we define a signs[] array.

O(n) also exists.

"""

def wiggle_subsequence(nums):
    """
    purpose is to print length of longest subsequence
    such that it's numbers are alternate larger , smaller or vice versa.
    """
    n = len(nums)
    if n == 0:
        return 0
    L = [1 for _ in range(n)]
    sign = [-1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if sign[j] == -1 and L[j] + 1 > L[i] and nums[j] != nums[i]:
                L[i] = L[j] + 1
                sign[i] = nums[j] < nums[i]
            elif nums[j] < nums[i] and sign[j] is False and L[j] + 1 > L[i]:
                L[i] = L[j] + 1
                sign[i] = True
            elif nums[j] > nums[i] and sign[j] is True and L[j] + 1 > L[i]:
                L[i] = L[j] + 1
                sign[i] = False

    return max(L)


# nums = [1, 2, 1, 1]
# nums = [1, 1, 1, 1, 1]
nums = [1,7,4,9,2,5]
nums = [1,17,5,10,13,15,10,5,16,8]
nums = [1,2,3,4,5,6,7,8,9]
print(wiggle_subsequence(nums))
