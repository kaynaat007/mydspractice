'''
There are n houses evenly lined up on the street, and each house is beautifully painted. You are given a 0-indexed integer array colors of length n, where colors[i] represents the color of the ith house.

Return the maximum distance between two houses with different colors.

The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.

'''
from typing import List


def maxDistanceUtil(colors: List[int]) -> int:

    ans = 0
    n = len(colors)
    for i in range(n):
        for j in range(n):
            if colors[i] != colors[j]:
                ans = max(ans, abs(i-j))
    return ans

colorarray  = [1,1,1,6,1,1,1]
print(maxDistanceUtil(colorarray))

colorarray = [1,8,3,8,3]
print(maxDistanceUtil(colorarray))

colorarray = [0,1]
print(maxDistanceUtil(colorarray))


