


from collections import defaultdict


def brute_force(a, k):
    n = len(a)
    count = 0
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += a[j]
            if curr_sum % k == 0:
                count += 1
    return count



def main(a, k):

    ans = set()
    for j in [k, -k, 0]:
        ans = print_subarray_sum_equals_k(a, j, ans)
    return len(ans)


def print_subarray_sum_equals_k(a, k, subarrays):

    curr_sum = 0
    n = len(a)
    prefix_map = defaultdict(list)

    for i in range(n):

        curr_sum += a[i]

        if curr_sum == k:
            subarrays.add((0, i))
        else:
            if k > 0 and curr_sum % k == 0:
                subarrays.add((0, i))

        remaining_sum = curr_sum - k

        if remaining_sum in prefix_map:

            last_indices = prefix_map[remaining_sum]
            for j in last_indices:
                subarrays.add((j+1, i))

        prefix_map[curr_sum].append(i)

    # print(prefix_map)
    # print(subarrays)
    return subarrays


a = [1, 2, 3]
a = [1, -3, 1]
a = [2, -2, 0]

a = [4,5,0,-2,-3,1]

# a = [5, 0, -2, -3]
# a = [0, -5]
# a = [-1, 2, 9]
# a = [-5]
a = [7, 4, -10]
k = 5
print(main(a, k))
print(brute_force(a, k))
# print(print_subarray_sum_equals_k(a, k))

"""
  # 
        # remaining_sum = curr_sum + k
        # 
        # if remaining_sum in prefix_map:
        # 
        #     last_index = prefix_map[remaining_sum]
        #     subarrays.add((last_index + 1, i))
        # 
        # remaining_sum = curr_sum
        # 
        # if remaining_sum in prefix_map:
        #     last_index = prefix_map[remaining_sum]
        #     subarrays.add((last_index + 1, i))
"""