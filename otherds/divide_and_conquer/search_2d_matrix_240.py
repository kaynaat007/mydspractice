from bisect import bisect_left


def search(a, t, i, j):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, t, i, j)
    if i == len(a):
        return False
    if t == a[i]:
        return True
    return False


def searchMatrix(matrix, target):
    """

    """
    n = len(matrix)
    m = len(matrix[0])

    r = n - 1
    c = m - 1

    while r >= 0 and c >= 0:

        x = matrix[r][c]
        if target > x:
            return False
        if target == x:
            return True

        left_y = matrix[r][0]
        up_y = matrix[0][c]

        check1 = False
        check2 = False

        if left_y <= target <= x:
            check1 = search(matrix[r], target, 0, c)

        if up_y <= target <= x:
            for k in range(0, r+1):
                if matrix[k][c] == target:
                    check2 = True
                    break
        if check1 or check2:
            return True
        r = r - 1
        c = c - 1
    return False


matrix = [
    [1, 3, 5],
    [2, 4, 8]
]
t = 10


matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
t = 19
print(searchMatrix(matrix, target=t))







