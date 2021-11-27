"""

"""


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

            # while stack and e < heights[stack[-1]]:
            #     f = stack.pop()
            #     if stack:
            #         stack.pop()
            #     max_area = max(max_area, heights[f] * (i - f), heights[i] * (i - f + 1))
            #
            stack.append(i)
    if not stack:
        return max_area
    last_index = stack[-1]
    prev = -1
    for i, e in enumerate(stack):
        max_area = max(max_area, (last_index - prev) * heights[e])
        prev = e
    return max_area


heights = [1, 2, 3, 2]

# heights = [1, 1]
#
# heights = [2, 2, 3, 2]
#
heights = [2,1,5,6,2,3]
#
heights = [1]
#
# heights = [1, 1, 2, 2, 3, 3]
#
heights = [3, 2, 1, 1]
#
# heights = []
#
# heights = [2,1,2]

# heights = [4,2,0,3,2,5]
# heights = [0, 0, 0]
# heights = [0, 3, 3, 1,10]

heights = [3,6,5,7,4,8, 1, 0]
print(largestRectangleArea(heights))


