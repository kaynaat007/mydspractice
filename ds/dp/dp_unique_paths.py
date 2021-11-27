"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

recursive:

There are just two ways to get to a cell (i,j). either from left or from top cell.
Number of paths to cell(i,j) is thus sum of paths till cell(i,j-1) and cell(i-1, j).

Obstacles just say that there is no path if obstacles are present so while backtracking if
we encounter any cell as value of 1, we return 0 from there. We have hit a wall.

dp:
p
Now in dp we start from cell(0, 0).  Initialize the matrix for first row and first column.

if encounter any 1 in first row, then all cells after that cell are unreachable which we represent as 0 in c.
same for first column.

Then we iterate row by row and calculate c[i][j] depending on weather A[i][j] is 1 or not. if it is 1, you can't
reach cell (i, j) so c[i][j] = 0 else it's sum of c[i-1, j]  and c[i, j-1]

"""

def print_matrix(k):
    for i in range(len(k)):
        print(k[i])


def recursive_unique_paths(i, j, A):
    if i < 0 or j < 0 :
        return 0
    if A[i][j] == 1:
        return 0
    if i == 0 and j == 0:
        return 1
    return recursive_unique_paths(i-1, j, A) + recursive_unique_paths(i, j-1, A)


def dp_unique_paths(A):
    """
    bottom up approach lenge
    """
    m = len(A)
    n = len(A[0])
    c = [[0 for __ in range(n)] for _ in range(m)]
    if A[0][0] == 1:
        return 0
    if A[m-1][n-1] == 1:
        return 0

    c[0][0] = 1

    for i in range(1, n):
        if A[0][i] == 1:
            c[0][i] = 0
        else:
            c[0][i] = 1

        if c[0][i-1] == 0:
            c[0][i] = 0

    for i in range(1, m):
        if A[i][0] == 1:
            c[i][0] = 0
        else:
            c[i][0] = 1
        if c[i-1][0] == 0:
            c[i][0] = 0

    for i in range(1, m):
        for j in range(1, n):
            if A[i][j] != 1 :
                c[i][j] = c[i-1][j] + c[i][j-1]
            else:
                c[i][j] = 0
    return c[m-1][n-1]



A = [
  [0,0,0],
  [0,0,0],
  [0,0,0]
]
m = len(A)
n = len(A[0])

paths = recursive_unique_paths(m-1, n-1, A)
print(paths)
paths = dp_unique_paths(A)
print(paths)
