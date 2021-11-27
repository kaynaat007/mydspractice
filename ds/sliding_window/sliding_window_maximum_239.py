from collections import deque


def max_sliding_window(nums, k):

    output = []
    n = len(nums)

    q = deque(maxlen=k)

    for i in range(0, k): # solve for first k indices first.
        val = nums[i]
        while q and nums[q[-1]] < val:
            q.pop()
        q.append(i)

    output.append(nums[q[0]])


    for i in range(k, n):

        val = nums[i]

        while q and q[0] < i - k + 1:  # an index out of the k window is thrown out. cannot contribute for maximum
            q.popleft()

        while q and nums[q[-1]] < val: # a value < incoming val is thrown out, cannot contribute for maximum in current
            # window
            q.pop()

        q.append(i)  # add the incoming index
        output.append(nums[q[0]])  # store the result.

    return output


nums = [1, 2, 3]
k = 3

nums = [1,3,-1,-3,5,3,6,7]
k = 3

nums = [0, 0, 12, 0]
k = 1
print(max_sliding_window(nums, k))