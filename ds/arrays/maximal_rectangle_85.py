from typing import List

def largestRectangleArea(heights: List[int]) -> int:
    stack = []
    max_area = 0
    n = len(heights)
    for i, e in enumerate(heights):
        if not stack:
            stack.append(i)
        elif e >= heights[stack[-1]]:
            stack.append(i)
        else:
            max_index = stack[-1]
            while stack and e < heights[stack[-1]]:
                top = stack[-1]
                stack.pop()
                if stack:
                    prev = stack[-1]
                else:
                    prev = -1
                max_area = max(max_area, (max_index - prev) * heights[top])
            stack.append(i)
    if not stack:
        return max_area
    last_index = stack[-1]
    prev = -1
    for i, e in enumerate(stack):
        max_area = max(max_area, (last_index - prev) * heights[e])
        prev = e
    return max_area


def maximalRectangle(matrix: List[List[str]]) -> int:
    """
    maximal rectangle is solved by using largest rectangle problem
    Call maximal rectangle in 1 D for each row of this matrix
    """

    if not matrix:
        return 0
    n = len(matrix)
    m = len(matrix[0])
    heights = [0 for _ in range(m)]
    max_area = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '1':
                heights[j] += 1
            else:
                heights[j] = 0
        # print(heights)
        max_area = max(max_area, largestRectangleArea(heights))
    return max_area


matrix = [['1'], ['1']]
matrix = [['1', '0', '1']]
matrix = [['1'], ['0'], ['1']]
matrix = [['1', '0', '1', '1']]
matrix = [['0', '1', '1', '1']]
# matrix  = [['1', '1'], ['1', '1']]
# matrix = [['1', '1', '1'], ['1', '1', '1'], ['1', '1', '1']]
matrix = [['1', '1', '0'], ['0', '1', '1']]
# matrix = [['1', '1'], ['0', '1']]
# matrix = [['0', '1'], ['0', '1']]
# matrix  = [['1', '0'], ['1', '0']]
# matrix = [['0', '1'], ['1', '1']]
# matrix = [['1', '0'], ['1', '1']]
# matrix = [['1', '0'], ['0', '1']]
# matrix = [['1', '1'], ['1', '1']]
# matrix = [['1', '1', '1'], ['0', '1', '1']]
# matrix = [['1', '1', '0'], ['1', '1', '1']]
# matrix = [['0', '1', '0'], ['1', '1', '1']]
# matrix = [['0', '0', '1'], ['1', '1', '1']]
# matrix = [['0', '1', '0'], ['0', '1', '0'], ['0', '1', '0']]

# matrix  = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# matrix = [["0","0","0","0","0","0","1"],["0","0","0","0","1","1","1"],["1","1","1","1","1","1","1"],["0","0","0","1","1","1","1"]]
# matrix = [["0","0"]]
print(maximalRectangle(matrix))





