

def swap(nums, i, j):

    x = nums[i]
    nums[i] = nums[j]
    nums[j] = x


def remove_duplicates(nums):

    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return 1
    slow = 0
    fast = slow + 1
    while fast < n:


        while slow < n and fast < n and nums[slow] == nums[fast]:
            fast += 1

        if slow + 1 < n and fast < n:
            swap(nums, slow + 1, fast)
        else:
            break
        slow = slow + 1
        fast = fast + 1

    return slow + 1

nums = [0, 0, 0, 0,  1, 1]
nums = [0, 0, 1]
nums = [0, 0, 1, 1, 1, 2, 2, 3,3, 3, 3, 3, 3]
print(remove_duplicates(nums))

