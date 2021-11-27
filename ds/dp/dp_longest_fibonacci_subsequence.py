"""

O(n^2) solution uses this recurrence

let dp[i][j] represent a fibonacci sequence ending at A[i] and A[j].

then dp(a, b) = 1 + dp(b-a, a) or 2 if b-a is not found in given array A.


"""

from bisect import bisect_left
from collections  import defaultdict

def print_matrix(k):
    for i in range(len(k)):
        print(k[i])



def find_longest_fibonacci_subsequence(A):

    n = len(A)

    if n <= 2:
        return 0

    max_length_so_far = 0
    for i in range(n):
        for j in range(i+1, n):
            target = A[i] + A[j]
            c = 2
            low = j+1
            prev = A[j]
            while low <= n:
                pos = bisect_left(A, target, lo=low, hi=n)
                if pos == n:
                    break
                if A[pos] == target:
                    c += 1
                    low = pos + 1
                    target = target + prev
                    prev = A[pos]
                else:
                    break

            if max_length_so_far < c:
                max_length_so_far = c

    if max_length_so_far == 2:
        return 0
    return max_length_so_far


def hash_based_LFS(A):

    n = len(A)

    if n <= 2:
        return 0

    seen = defaultdict()
    for i in range(n):
        seen[A[i]] = i

    dp = [[0 for _ in range(n) ] for _ in range(n-1)]
    max_lfs = 0
    for i in range(1, n):
        dp[0][i] = 2

    for i in range(1, n-1):
        for j in range(i+1, n):
            val = A[j] - A[i]
            if val in seen and seen[val] < i:
                dp[i][j] = dp[seen[val]][i] + 1
            else:
                dp[i][j] = 2
            if max_lfs < dp[i][j]:
                max_lfs = dp[i][j]

    if max_lfs <= 2:
        return 0
    return max_lfs






A = [1, 2, 3, 5]
# A = [1,2,3,4,5, 8]
# A = [1,3,7,11,12,14,18]
# A = [4, 5, 9, 13, 18, 22, 35]

# A = [1, 2, 3]

A = [2,4,7,8,9,10,14,15,18,23,32,50]
print(hash_based_LFS(A))




