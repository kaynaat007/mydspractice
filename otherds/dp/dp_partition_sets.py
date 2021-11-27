def print_matrix(k):
    print('---------------------------')
    for i in range(len(k)):
        print(k[i])


def dp_partition_equal_set(A):

    total_sum = sum(A)
    if total_sum % 2 != 0:
        return False

    target = int(total_sum/2)

    n = len(A)
    dp = [[False for _ in range(target  + 1) ] for _ in range(n)]
    for i in range(target + 1):
        if i == A[0]:
            dp[0][i] = True

    for i in range(n):
        dp[i][0] = True

    for i in range(1, n):
        for j in range(1, target + 1):
            if j - A[i] < 0:
                dp[i][j] = dp[i-1][j]
            else:
                if dp[i-1][j] or dp[i-1][j-A[i]]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False
    return dp[n-1][target]


# A = [1, 5, 11, 5]
A = [1, 2, 3, 5]
# A = [1, 1]
print(dp_partition_equal_set(A))
