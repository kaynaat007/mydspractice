

def recursive_rob_house(A, n):
    """

    """
    if n < 0:
        return 0
    if n == 0:
        return A[0]
    return max(

        A[n] + recursive_rob_house(A, n-2), A[n-1] + recursive_rob_house(A, n-3)
    )


def dp_bottom_up_rob_houses(A):
    """
    money[i] indicates the maximum amount of money you will be able to
    rob by robbing houses numbered from 0...i
    money[n-1] is our answer
    """
    n = len(A)
    if n == 0:
        return 0
    if n == 1:
        return A[0]

    money = [0 for _ in range(n)]
    money[0] = A[0]
    money[1] = max(A[0], A[1])
    for i in range(2, n):
        money[i] = max( A[i] + money[i-2], A[i-1] + money[i-3])

    return money[n-1]


# A = [1,2,3,1]
A = [2,7,9,3,1]
n = len(A) - 1

print(recursive_rob_house(A, n))
print(dp_bottom_up_rob_houses(A))