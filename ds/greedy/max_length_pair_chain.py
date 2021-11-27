import math



def max_length_pair_chain(pairs):
    n = len(pairs)
    if n == 0:
        return 0
    if n == 1:
        return 1
    pairs = list(sorted(pairs, key=lambda x: x[1]))
    end_so_far = -math.inf
    c = 0
    ans = []
    for i in range(n):
        start, end = pairs[i]
        if start > end_so_far:
            c += 1
            end_so_far = end
            ans.append((start, end))
    return c


pairs = [[1,2], [2,3], [3,4]]
# pairs = [[1, 2], [6, 7], [5, 8], [9, 12], [10, 11]]
print(max_length_pair_chain(pairs))




