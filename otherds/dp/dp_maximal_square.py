""""

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

find the area  of maximal square with all 1's.
ans = 4

base cases :

1 means 1 by 1 square

all 4 1 in
1 1
1 1 means 2 by 2 square

how can we get a 3 by 3 square from a 2 by 2 square ?

setup a convention. look at an element on matrix and three elements beside it


top (i-1, j)
diagnaol (i-1, j-1)
left (i, j-1 )

these three elements determine the dimension of square at index (i, j)

if any of these elements is zero, you chance of making a bigger square at i,j  is gone.

so if dimensions of squares at these indexes is say 1 by 1, 2 by 2 and 2 by 2, what can you say
about dimension of square at index (i, j). ?

a 1 at position (i, j) will contribute for an extra dimesnion but to which square ?
The one with minimum dimension. !

check on paper for yourself to see that. !  



"""

def print_matrix(k):
    for i in range(len(k)):
        print(k[i])


def find_maximal_square(matrix):
    """

    """
    n = len(matrix)
    m = len(matrix[0])
    dp = [[0 for _ in range(m)] for _ in range(n)]
    matrix = [[int(matrix[i][j]) for j in range(m)] for i in range(n)]
    max_dimension = 0

    for i in range(m):
        if matrix[0][i] == 1:
            dp[0][i] = 1
            max_dimension = 1

    for i in range(n):
        if matrix[i][0] == 1:
            dp[i][0] = 1
            max_dimension = 1

    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == 0:
                dp[i][j] = 0
            else:
                min_dimension = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j])
                dp[i][j] = 1 + min_dimension
                max_dimension = max(max_dimension, dp[i][j])

    return max_dimension * max_dimension


matrix = [
    [1, 0, 1, 0, 0],
    [1,  0,  1,  1, 1],
    [1,  1,  1,  1, 1],
    [1, 0, 0, 1,  0]
]

print(find_maximal_square(matrix))
