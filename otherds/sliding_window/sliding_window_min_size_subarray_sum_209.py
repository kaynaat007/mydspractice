import math
from math import floor


def min_size_subarray(t, nums):

    n = len(nums)
    if n == 0:
        return 0

    prefix_sum = [0] * n
    prefix_sum[0] = nums[0]
    for i in range(1, n):
        prefix_sum[i] = nums[i] + prefix_sum[i-1]

    curr_sum = nums[0]
    l = 0
    r = 0

    ans = n * 2

    while l < n and r < n:

        while curr_sum < t and r < n:
            r += 1
            if r < n:
                curr_sum += nums[r]

        if curr_sum >= t:
            # r and l
            k = l
            while prefix_sum[r] - prefix_sum[k] >= t:
                k = k + 1
            l = k
            ans = min(r - l + 1, ans)

            if l == r:
                l += 1
                r += 1
                if l < n:
                    curr_sum = nums[l]
            else:
                l = l + 1
                curr_sum = prefix_sum[r] - prefix_sum[l - 1]
        else:
            break

    if ans == 2 * n:
        return 0
    return ans


def min_subarray_util(s, nums, i, j, n,  prefix_sum):

    if i == j:
        return i, i, -1

    if i > j:
        return -1, -1, -1

    mid = floor(i + (j-i)/2)
    print('i , j,  mid ', i, j, mid)
    min_size = math.inf

    left_start, left_end, _  =  min_subarray_util(s, nums, i, mid-1, n,  prefix_sum)
    right_start, right_end, _ = min_subarray_util(s, nums, mid+1, j, n, prefix_sum)

    right_sum = 0
    left_sum = 0

    if right_end >= 0 and right_start-1 >= 0:
        right_sum = prefix_sum[right_end] - prefix_sum[right_start-1] + nums[mid]
    if left_start - 1 >= 0 and left_end >= 0:
        left_sum = prefix_sum[left_end] - prefix_sum[left_start-1]

    if right_sum >= s:
        min_size = min(min_size, right_end - right_start + 1)
    if left_sum >= s:
        min_size - min(min_size, left_end - left_start + 1)

    right_size = right_end - right_start + 1

    m = 1
    for k in range(left_end, left_start-1, -1):
        if k >= 0:
            if nums[k] + right_sum >= s:
                min_size = min(min_size, right_size + m)
            m = m + 1

    return i, j, min_size


def nlogn_minimum_size_subarray_sum(s, nums):

    n = len(nums)
    prefix_sum = [0] * n
    prefix_sum[0] = nums[0]
    for i in range(1, n):
        prefix_sum[i] = nums[i] + prefix_sum[i - 1]
    return min_subarray_util(s, nums, 0, n-1, n, prefix_sum)



# t = 20

t = 2
nums = [1, 1, 2]

# t = 7
# nums = [2,3,1,2,4,3]

# t = 10
# nums = [2, 3, 2, 3]

# nums = []
#
# t = 20
# nums = [2,16,14,15]

print(min_size_subarray(t, nums))

t = 3
nums = [1, 2]
i, j, min_size = nlogn_minimum_size_subarray_sum(t, nums)
print(min_size)

