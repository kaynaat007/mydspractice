from typing import List
from collections import defaultdict


def countGoodRectangles(rectangles: List[List[int]]) -> int:

    count = defaultdict(int)
    max_key = -1
    for rectangle in rectangles:
        square = min(rectangle[0], rectangle[1])
        count[square] += 1
        if square > max_key:
            max_key = square
    return count[max_key]


rectangles = [[5,8],[3,9],[5,12],[16,5]]

# rectangles = [[2,3],[3,7],[4,3],[3,7]]
# rectangles = [[5,8],[3,9],[3,12]]
print(countGoodRectangles(rectangles))

