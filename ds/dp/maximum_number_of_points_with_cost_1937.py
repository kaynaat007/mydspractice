from typing import List
import math

"""
issue is with last example as showm
we don't know which top 5 lead to an answer 
need to track indexes of 5 
"""


def maxPoints(points: List[List[int]]) -> int:

    n = len(points)
    m = len(points[0])
    dp = [0 for _ in range(n)]
    max_e = -1 * math.inf
    max_index = -1
    for i in range(m):
        if points[0][i] > max_e:
            max_e = points[0][i]
            max_index = i
    dp[0] = max_index
    current_sum = max_e
    # print(current_sum, max_index)

    for i in range(1, n):
        max_e = -1 * math.inf
        max_index = -1
        for j in range(m):
            if current_sum - abs(dp[i-1] - j) + points[i][j] > max_e:
                max_e = current_sum - abs(dp[i-1] - j) + points[i][j]
                max_index = j
        dp[i] = max_index
        current_sum = max_e
    print(dp)
    return current_sum


def maxPoints2(points: List[List[int]]) -> int:
    n = len(points)
    m = len(points[0])
    print('solution v2..')
    dp = [0 for _ in range(m)]
    v = []
    for i in range(m):
        dp[i] = points[0][i]
    for i in range(1, n):
        for j in range(m):
            max_e = -1 * math.inf
            for k in range(m):
                max_e = max(dp[k] - abs(k - j), max_e)
            v.append(max_e + points[i][j])
        dp = v.copy()
        v.clear()
    # print(dp)
    return max(dp)


def calculate_left(pre, n):

    curr = [0 for _ in range(n)]
    curr[0] = pre[0]

    for i in range(1, n):
        curr[i] = max(pre[i], curr[i-1]-1)

    return curr


def calculate_right(pre, n):
    curr = [0 for _ in range(n)]
    curr[n-1] = pre[n-1]

    for i in range(n-2, -1, -1):
        curr[i] = max(pre[i], curr[i+1]-1)

    return curr


def maxPointsV3(points):
    # print('solutions v3..')
    n = len(points)
    m = len(points[0])
    curr = [0 for _ in range(m)]
    pre = []

    for i in range(m):
        pre.append(points[0][i])

    for i in range(1, n):
        left = calculate_left(pre, m)
        right = calculate_right(pre, m)
        # print(left, right)
        for j in range(m):
            curr[j] = points[i][j] + max(left[j], right[j])
        # print("curr", curr)
        pre = curr.copy()
    # print(pre)
    return max(pre)




points = [[1], [2]]
points = [[1, 2], [3, 4]]
# points = [[1,2,3],[1,5,1],[3,1,1]]
# points  = [[1,5],[2,3],[4,2]]
points = [[2,3,4], [1,0,1], [9,10,13], [4, 1, 0], [5, 6, 2]]
# points  = [[5,2,1,2],[2,1,5,2],[5,5,5,0]]
points = [[2,4,0,5,5],[0,5,4,2,5],[2,0,2,3,1],[3,0,5,5,2]]  #17

print(maxPoints2(points))
print(maxPointsV3(points))

