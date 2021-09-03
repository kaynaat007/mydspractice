from typing import List

def b_search(arr, low, high, n, target):

    # print('searching between {} and {}'.format(low, high))
    if low > high:
        return None

    if high - low + 1 == 1:
        if target <= arr[low]:
            return high + 1
        else:
            return high

    mid = low + (high - low) // 2

    if 1 <= mid < n and target > arr[mid]:
        return b_search(arr, low, mid - 1, n, target)
    else:
        return b_search(arr, mid + 1, high, n, target)


def countSmaller(nums: List[int]) -> List[int]:

    stack = []
    count = []
    for e in reversed(nums):
        if not stack:
            stack.append(e)
            count.append(0)
        elif e > stack[-1]:
            stack.append(e)
            count.append(count[-1] + 1)
        else:
            stack.append(stack[-1])
            stack = list(reversed(stack))
            idx = b_search(stack, 0, len(stack)-1, len(stack), e)
            if idx == len(stack):
                count.append(0)
            else:
                count.append(count[idx] + 1)
    return count

nums = [5, 3, 2, 1]
nums = [1, 2, 3, 4, 5]

nums = [5, 2, 3]
c = countSmaller(nums)
print(list(reversed(c)))



#
# target = 8
# return b_search(nums, 0, len(nums)-1, len(nums), target)
#
#
# nums = [10, 6, 5, 5]
# nums = [8, 8, 5, 5, 5, 5]
# print(countSmaller(nums))