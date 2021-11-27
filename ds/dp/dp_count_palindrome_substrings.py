"""

"""


def print_matrix(k):
    for i in range(len(k)):
        print(k[i])

def construct_is_palindrome(A):
    """

    """
    n = len(A)
    is_palin = [ [False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        is_palin[i][i] = True
    for l in range(2,  n+1):
        i = 0
        for j in range(l-1, n):
            print(i, j)
            if i + 1 <= j - 1:
                is_palin[i][j] = A[i] == A[j] and is_palin[i+1][j-1]
            else:
                is_palin[i][j] = A[i] == A[j]
            i =  i + 1
    return is_palin


def dp_count_palin_substring(A):
    n = len(A)
    is_palin = construct_is_palindrome(A)
    print_matrix(is_palin)
    c = n
    for l in range(2, n + 1):
        i = 0
        for j in range(l - 1, n):
            if is_palin[i][j]:
                print(i, j)
                c += 1
            i += 1
    return c


def dp_count_palin_v2(A):
    n = len(A)

    is_palin = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        is_palin[i][i] = True
    c = n

    for l in range(2, n + 1):
        i = 0
        for j in range(l - 1, n):
            # print(i, j)

            if i + 1 <= j - 1:
                is_palin[i][j] = A[i] == A[j] and is_palin[i + 1][j - 1]
            else:
                is_palin[i][j] = A[i] == A[j]
            # print(is_palin[i][j])
            if is_palin[i][j]:
                # print(i, j)
                c += 1
            i += 1
    return c


A = 'aaa'
print(dp_count_palin_v2(A))
