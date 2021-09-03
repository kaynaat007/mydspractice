def print_matrix(k):
    for i in range(len(k)):
        print(k[i])

def fixed_partitioning(A, i, n, k):
    """

    """
    # print('paritioning at i, n, k', i, n, k)
    if k <=0:
        return 0

    if k == 1 and i >= 0:
        av = sum(A[i::-1])/(i+1)
        return av

    max_av = 0
    for j in range(i, -1, -1):

        if j == 0:
            s = sum(A[n-1::-1])
        else:
            s = sum(A[n-1:j-1: -1])

        av_right = s/(n-j)
        av_left = fixed_partitioning(A, j-1, n-1, k-1)

        av = av_left + av_right
        max_av = max(max_av, av)

    return max_av


def main(A, k):
    n = len(A)
    max_av = 0
    if k > n:
        return 0
    for i in range(1, k+1):
        av = fixed_partitioning(A, n-1, n, i)
        max_av = max(av, max_av)
    return max_av


def dp_largest_average(A, k):

    n = len(A)
    if k == 1:
        return sum(A)/n

    if k > n:
        return 0

    dp = [[0 for _ in range(n) ] for _ in range(k+1)]

    s = 0
    for i in range(n):
        s = s + A[i]
        dp[1][i] = s/(i+1)

    freq = [0 for _ in range(n)]
    freq[0] = A[0]
    for i in range(1, n):
        freq[i] = freq[i-1] + A[i]

    for i in range(2, k+1):

        for j in range(1, n):
            if i > j + 1:
                continue
            if i == j+1:
                dp[i][j] = freq[j]
                continue

            m = j
            max_avg = 0
            s = 0

            while m >= 0 and i - 1 <= m:

                s = s + A[m]
                left_avg = dp[i-1][m-1]
                right_avg = s/(j + 1 - m)
                max_avg = max(max_avg, left_avg + right_avg)
                m -= 1
            dp[i][j] = max_avg

    max_avg = 0
    for i in range(1, k+1):
        if max_avg < dp[i][n-1]:
            max_avg = dp[i][n-1]
    return max_avg




# A = [9, 1, 2, 3, 9]
# A = [10, 12]
A = [9, 1, 3, 4, 5, 6, 7, 10, 100, 23, 45]
A = [9, 1, 3, 4, 5, 6, 7, 10, 100, 23]
# A = [9, 1, 2]
k = 3
n = len(A)
print(main(A, k))
print(dp_largest_average(A, k))

