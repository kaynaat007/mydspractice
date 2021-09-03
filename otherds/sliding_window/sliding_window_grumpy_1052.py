"""
Fixed window problem.

two parts:
    maximize the customers satisfied when grumpy[j] == 1 with given x.
    sum of all other parts where grumpy[j] == 0

we tjaje
"""


def grumpy(customers, grumpy, x):

    slow = 0
    fast = 0 + x - 1
    ans = 0
    satisfied = 0
    optimal_window_start = 0
    n = len(customers)
    curr_sum = 0

    while fast < n:
        j = slow

        if curr_sum > 0:
            if grumpy[fast] == 1:
                curr_sum = curr_sum + customers[fast]
            if grumpy[slow-1] == 1:
                curr_sum = curr_sum - customers[slow-1]
        else:
            while j <= fast:
                if grumpy[j] == 1:
                    curr_sum += customers[j]
                j = j + 1

        if curr_sum > ans:
            optimal_window_start = slow
            ans = curr_sum

        slow = slow + 1
        fast = fast + 1

    for i in range(n):

        if optimal_window_start <= i <= optimal_window_start + x - 1:
            if i <= n-1:
                satisfied += customers[i]
        else:
            if grumpy[i] == 0:
                satisfied += customers[i]
    return satisfied

cust = [1,0,1,2,1,1,7,5]
gr = [0,1,0,1,0,1,0,1]

cust = [2, 3, 4, 1]
gr = [1, 1, 1, 1]
x = 3

print(grumpy(cust, gr, x))
