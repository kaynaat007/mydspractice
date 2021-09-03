
# simple stack o

def nextGreaterElementsV1(nums):

    if not nums:
        return []
    stack = []
    n = len(nums)
    if n == 1:
        return [-1]
    output = [0 for i in range(n)]
    j = 1
    stack.append((0, nums[0]))

    while True:

        val = nums[j]
        t, top = stack[-1]

        # step 1: knock off whatever you can

        while stack and val > top:
            output[t] = val
            stack.pop()
            if stack:
                t, top = stack[-1]

        # step 2:  check if it is time to terminate the loop
        if stack:
            f, first = stack[0]  # if incoming elements index is equal to
            # stacks first element index, we have come round trip
            # we do not want to add the same element again. so we break
            if j == f:
                break

        # step 3: now add the incoming element to stack
        stack.append((j, val))
        j = (j + 1) % n

    while stack:
        k, val = stack.pop()
        output[k] = -1

    return output


# two pass approach




nums = [6, 8, 10]
# nums = [8,  6, 4]
# nums = [6, 8, 4]
nums = [1, 2, 1]
# nums = [i for i in range(100000)]
# nums = [8, 6, 5]
# nums = [5, 6, 1]
# nums = [5, 8, 8, 10]
# nums = [8, 8, 8]

nums = [4, 6, 4]
# nums = [6, 6, 4, 6, 6]
# nums = [4, 4, 6, 4, 4]
# nums = [4, 6, 1]
# nums = [4, 4, 6, 6]
# nums = [6, 6, 4, 4]
# nums = [6, 6, 2, 8]

# nums = [0, 0, 0, 1]
# nums = [1,2,3,4,3]
# nums = []
# nums = [1, ]
print(nextGreaterElementsV1(nums))
