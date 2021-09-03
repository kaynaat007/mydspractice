"""
find length of longest arithmatic progression

problem follows similar structure as of LIS.
Like LIS, the longest increasing subsequence length at index i depends on
all LIS at index j wherever a[j] < a[i],

here Length of AP ( not longest ) at index i, depends on all indexes j < i

wherever following condition holds:

    if we have another AP ending at index j with a difference d
    and this d == A{i] - A{j]
    This means A[i] is added to existing AP at index j.
    so length get increased by 1 at index i.

   so at each index j < i we need to store the difference d and length of AP ending at that index j.
   so a dictionary at index j
   such  that key is the difference and value is length of AP at that index.
   Note that minimum value at a given index j in this dict for a given d can be 2, since two elements always form
   a AP.

"""


def util(a, j, d, n):
    if j == n:
        return 0
    for k in range(j+1, n):
        if d == a[k] - a[j]:
            return 1 + util(a, k, d, n)
    return 0


def recursive_llap(a):
    """

    """
    n = len(a)
    l = 1
    for i in range(0, n):
        for j in range(i+1, n):
            d = a[j] - a[i]
            l = max(2 + util(a, j, d, n), l)
    return l


def linear_llap(a):

    n = len(a)
    l_max = 1
    for i in range(0, n):
        for j in range(i + 1, n):
            d = a[j] - a[i]
            l = 2
            for k in range(j+1, n):
                if a[j] + (l-1) * d == a[k]:
                    l += 1
            l_max = max(l_max, l)

    return l_max


def dp_llap(a):
    """

    """
    l_max = 1
    n = len(a)
    if n == 0:
        return 0
    d = [{} for i in range(n)]
    for i in range(1, n):
        l = 1
        for j in range(0, i):
            diff = a[i] - a[j]
            if d[j].get(diff):
                d[i][diff] = d[j][diff] + 1
            else:
                d[i][diff] = 2
            l = max(l, d[i][diff])
        l_max = max(l, l_max)
    return l_max


a = [20, 1, 15, 3, 10, 5, 8]
# a = [1, 7, 10, 15, 27, 29]
# a = [5, 10, 15, 20, 25, 30]

# a = [1 , 7,  12,  13,  14]
# a = [0, 2, 4, 7, 9, 10, 20]
# a = [2, 7, 10, 13, 14, 19]
print(recursive_llap(a))
print(linear_llap(a))
print(dp_llap(a))