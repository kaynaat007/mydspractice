
def count_squares(matrix):

    n = len(matrix)
    m = len(matrix[0])
    count = [ [0 for _ in range(m)] for _ in range(n)]

    total_count = 0
    if n == 0 or m == 0:
        return 0

    if matrix[0][0] == 1:
        count[0][0] = 1
        total_count = 1

    for i in range(1, m):
        if matrix[0][i] == 1:
            count[0][i] = 1
            total_count += 1

    for j in range(1, n):
        if matrix[j][0] == 1:
            count[j][0] = 1
            total_count += 1

    for i in range(1, n):
        for j in range(1, m):
            k = min(count[i-1][j-1], count[i-1][j], count[i][j-1])
            if matrix[i][j] == 1:
                count[i][j] = 1 + k
                total_count += 1 + k
    return total_count



matrix  = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

matrix = [
  [1,0,1],
  [1,1,0],
  [1,1,0]
]

# matrix = [[]]

print(count_squares(matrix))

