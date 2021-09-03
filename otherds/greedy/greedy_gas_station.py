
def greedy_gas_station(gas, cost):

    i = 0

    gas_sum = sum(gas)
    cost_sum = sum(cost)
    n = len(gas)

    if gas_sum < cost_sum:
        return -1

    diff = []
    visited = []
    for alpha, beta in zip(gas, cost):
        delta = alpha - beta
        if delta > 0:
            visited.append(i)
        diff.append((delta,  i))
        i += 1
    slow = visited[0]
    curr_sum = diff[slow]
    fast = slow
    visited_count = 0
    i = 0

    while fast != slow -1:

        while curr_sum >= 0 and fast != slow -1:

            fast = (fast + 1) % n
            curr_sum = curr_sum + diff[fast]

        if fast == slow - 1:
            break
        else:
            visited_count += 1

            while curr_sum < 0 and slow <= fast:
                curr_sum = curr_sum - diff[slow]
                slow += 1

        slow += 1
        fast += 1







gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

# gas = [2,3,4]
# cost = [3,4,3]

gas = [6, 1, 2, 5, 3, 7]
cost = [3, 2, 3, 3, 1, 8]

gas = [5,8,2,8]
cost = [6,5,6,6]

print(greedy_gas_station(gas, cost))