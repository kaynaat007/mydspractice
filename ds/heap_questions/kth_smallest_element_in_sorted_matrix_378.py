from typing  import List
import heapq


def kthSmallest(matrix: List[List[int]], k: int) -> int:


    n = len(matrix)
    m = len(matrix[0])
    heap = []
    for i in range(m):
        heapq.heappush(heap, (matrix[0][i], i, (0, i)))
    s = 0
    element = -1
    while s < k:
        element, counter, pos = heapq.heappop(heap)
        s += 1
        counter += 1
        i = pos[0]
        j = pos[1]
        if i + 1 < n:
            heapq.heappush(heap, (matrix[i+1][j], counter, (i+1, j)))
    return element

matrix= [

    [1, 2, 3],
    [3, 5, 6]
]

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]

k = 8
print(kthSmallest(matrix, k))







