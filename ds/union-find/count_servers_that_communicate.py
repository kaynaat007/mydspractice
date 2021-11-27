from collections import Counter
from typing import List


class UF:

    def __init__(self, components):
        self.components = components
        self.size = [1 for _ in range(len(components))]

    def find(self, element):

        while self.components[element] != element:
            element = self.components[element]

        return element

    def union(self, element1, element2):
        root1 = self.find(element1)
        root2 = self.find(element2)

        if root1 != root2:
            if self.size[root1] < self.size[root2]:
                self.components[root1] = root2
                self.size[root2] += self.size[root1]
            else:
                self.components[root2] = root1
                self.size[root1] += self.size[root2]


def countServers(grid: List[List[int]]) -> int:
    n = len(grid)
    m = len(grid[0])
    k = 0
    components = []
    for i in range(n):
        for j in range(m):
            components.append(k)
            k = k + 1

    uf = UF(components)

    k = 0
    for i in range(n):
        first = None
        second = None
        for j in range(m):
            if grid[i][j] == 1:
                if first is None:
                    first = k
                    k = k + 1
                    continue
                if first is not None:
                    second = k
                if (first is not None) and (second is not None):
                    uf.union(first, second)
                    first = second
            k = k + 1

    q = 0
    for i in range(m):
        k = q
        first = None
        second = None
        for j in range(n):
            if grid[j][i] == 1:
                if first is None:
                    first = k
                    k = k + m
                    continue
                if first is not None:
                    second = k
                if (first is not None) and (second is not None):
                    uf.union(first, second)
                    first = second
            k = k + m
        q = q + 1

    count = {}
    for i in range(len(components)):
        r = uf.find(i)
        if uf.size[r] > 1 and r not in count:
            count[r] = uf.size[r]

    # print(components)
    # print(uf.size)
    # print(Counter(components))
    # print(count)

    return sum(count.values())


grid = [[1,0],[0,1]]

# grid = [[1,0],[1,1]]

# grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]

# grid = [[1,1],[1,1]]

# grid = [[1,1]]

grid = [[1, 1, 1], [1, 1, 1], [1, 1, 0]]

print(countServers(grid))


