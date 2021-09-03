

def longest_subarray(nums, limit):

    n = len(nums)
    slow = 0
    fast = 0
    ans = 0
    current_highest = 0
    current_smallest = 0
    next_smallest_index = 0
    curr_length = 0
    smallest_index = 0

    while slow < n and fast < n:

        if nums[fast] > nums[current_highest]:

            current_highest = fast

        elif nums[fast] < nums[current_smallest]:

            current_smallest = fast

        if abs(nums[current_highest] - nums[current_smallest]) <= limit:
            curr_length += 1
            fast += 1
        else:
            ans = max(ans, curr_length)
            curr_length = 0
            slow = max(current_highest, current_smallest)
            fast = slow
            current_smallest = slow
            current_highest = slow

        ans = max(ans, curr_length)

    return ans

# nums = [2, 2]
# limit = 1  # ex 2

nums = [8, 2, 4, 7]
limit = 4  # ex 2

nums = [10,1,2,4,7,2]
limit = 5  # ex 4

# nums = [4,2,2,2,4,4,2,2]
# limit = 0  # ex 3

print(longest_subarray(nums, limit))