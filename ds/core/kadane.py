"""
Kadane's algorithm

Let M(i) represent maximum sum of subarray ending at i-1
M(0) = 0

Let the current element scanned by e

M(i) = max( M(i-1)  + e,  0 )

"""


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


def find_maximum_subarray(arr):

    current_max_sum = 0
    prev_max_sum = 0
    n = len(arr)
    ans = 0
    for i in range(n):
        current_max_sum = max(prev_max_sum + arr[i], 0)
        prev_max_sum = current_max_sum
        if current_max_sum > ans:
            ans = current_max_sum
    return ans


print(find_maximum_subarray(arr))



