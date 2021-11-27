from typing import List

'''

staircase pattern
. . - 
. - - 
- - -  
'''


def countNegatives(grid: List[List[int]]) -> int:
    """
    n + m work  
    """

    if not grid:
        return 0
    n = len(grid)
    m = len(grid[0])
    i = 0
    j = m-1
    count = 0
    while i < n and j >= 0:

        val = grid[i][j]
        if val < 0:
            count += (n - i)
            j -= 1
        else:
            i += 1

    return count

grid = [[2, -1]]
grid = [[-1, -2]]
grid = [[1], [-2]]
grid = [[1], [0], [-1]]
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
grid = [[3,2],[1,0]]
grid = [[1,-1],[-1,-1]]
print(countNegatives(grid))
