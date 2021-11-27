"""
We slide the end of the window to the right with each step.
If the total sum exceeds the maxCost,
we slide the start of the window to the right until the total sum inside the window is less than maxCosts.
With each eligible window, we take the length and keep track of the maximum length.
"""


def within_budget_v2(s, t, max_cost):
    n = len(s)
    a = []
    for i in range(n):
        a.append(abs(ord(s[i]) - ord(t[i])))

    curr_sum = 0
    max_length = 0
    slow = 0
    for i in range(n):
        curr_sum += a[i]
        while curr_sum > max_cost:
            curr_sum -= a[slow]
            slow += 1
        max_length = max(max_length, i - slow + 1)
    return max_length




def within_budget(s, t, max_cost):
    """

    """
    n = len(s)
    a = []
    for i in range(n):
        a.append(abs(ord(s[i]) - ord(t[i])))

    # print(a)

    slow = 0
    fast = 0
    curr_sum = 0
    max_length = 0
    length = 0
    # if max_cost == 0:
    #     return 1

    while slow < n and fast < n:

        if fast < n and slow - 1 >= 0:

            curr_sum = curr_sum + a[fast] - a[slow-1]
            length = fast - slow + 1
            fast += 1
            while curr_sum < max_cost and fast < n:

                if curr_sum <= max_cost:
                    max_length = max(max_length, length)

                curr_sum += a[fast]
                length += 1
                fast += 1
            fast -= 1

        elif fast == 0:

            length = 0

            while curr_sum <= max_cost and fast < n:  # expand the current window

                curr_sum += a[fast]
                fast += 1
                length += 1
                if curr_sum <= max_cost:
                    max_length = max(max_length, length)

            fast = fast - 1

        if curr_sum <= max_cost:
            max_length = max(max_length, length)

        fast += 1
        slow += 1

    return max_length

# s = 'abcd'
# t = 'bcdf'
# max_cost = 3 # 3

# s = 'abcd'
# t = 'cdef'
# max_cost = 3 # 1
#

# s = 'abcd'
# t = 'acde'
# max_cost = 0 # 1

# # #
# s = "krrgw"
# t = "zjxss"
# max_cost = 19 # expected is 2

# s = "krpgjbjjznpzdfy"
# t = "nxargkbydxmsgby"
# max_cost = 14  # expected 4

s = "abcd"
t = "abcd"
max_cost = 0  # expected 4



# a = [10, 20, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 1, 1, 1, 1, 1]
# a = [10, 20, 30, 1, 1]
# [3, 6, 15, 11, 3, 9, 8, 15, 22, 10, 3, 7, 3, 4, 0]
print(within_budget_v2(s, t, max_cost))