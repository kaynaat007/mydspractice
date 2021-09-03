from typing import List

class UnionFind:

    def __init__(self, n):
        self.n = n
        self.tree = []
        self.size = []
        for i in range(self.n):
            self.tree.append(i)
            self.size.append(1)

    def find(self, index):

        root = index
        while self.tree[index] != index:
            root = self.tree[index]
            index = root
        return root

    def union(self, index1, index2):

        root1 = self.find(index1)
        root2 = self.find(index2)

        if self.size[index1] < self.size[index2]:
            self.tree[root1] = root2
            self.size[root2] += self.size[root1]
        else:
            self.tree[root2] = root1
            self.size[root1] += self.size[root2]

    def components(self):
        print('tree', self.tree)
        print('size', self.size)
        components = set()
        for i in range(self.n):
            components.add(self.find(i))
        return components


class Kruskal:
    """
    Used to find MST of graph

    MST = Tree connecting all vertices of graph such that it's cost is minimum
    Running time = mlogm + n-1 * U + 2m * F
    U =  2 * logN where N is #vertices
    F = logN
    T = mlogM + NlogN + 2m logN
    """

    def __init__(self, vertices, edges):
        """
        edges of graph as input
        each element of edges is (u, v, w)
        where w is weight of the edge connecting vertices u,v.
        vertices: count of vertices
        """

        self.edges = edges
        self.n = vertices
        self.output = []

    def execute(self):
        """
        sort edges in increasing order of weight
        set T = []
        for each edge e:
            let u, v be endpoints of edge
            root1 = find(u)
            root2 = find(v)
            if root1 != root2: # these two vertices are part of different component
                ADD edge e into T
                union(root1, root2)

        Condition to stop is when source and target vertex are connected

        """
        edges = sorted(self.edges, key=lambda x: x[2])
        uf = UnionFind(self.n)
        target_vertex = self.n - 1
        source_vertex = 0

        for u, v, weight in edges:
            root1 = uf.find(u)
            root2 = uf.find(v)
            source_root = uf.find(source_vertex)
            target_root = uf.find(target_vertex)
            if root1 != root2:
                if source_root != target_root: # as long as source and target vertex are not in the same set
                    self.output.append((u, v, weight))
                    uf.union(root1, root2)
                else:
                    # break since now source and target would be in the same set
                    print('breaking out..')
                    break


def get_edges(heights):

    n = len(heights)
    m = len(heights[0])
    elements = n * m
    edges = []
    result = [[0 for _ in range(m)] for _ in range(n)]
    result[0][0] = 0
    k = 0
    for i in range(n):
        for j in range(m):

            current_val = heights[i][j]
            upper_vertex = k - m

            if j == 0:
                left_vertex = None

            else:
                left_vertex = k - 1

            if j == m - 1:
                right_vertex = None
            else:
                right_vertex = k + 1

            down_vertex = k + m

            if upper_vertex >= 0:
                upper_val = heights[i - 1][j]
                edges.append((k, upper_vertex, abs(upper_val - current_val)))

            if left_vertex is not None and left_vertex >= 0:
                left_val = heights[i][j - 1]
                edges.append((k, left_vertex, abs(left_val - current_val)))

            if right_vertex is not None and right_vertex <= elements - 1:
                right_val = heights[i][j + 1]
                edges.append((k, right_vertex, abs(right_val - current_val)))

            if down_vertex <= elements - 1:
                down_val = heights[i + 1][j]
                edges.append((k, down_vertex, abs(down_val - current_val)))

            k += 1
    return edges



def minimumEffortPath(heights: List[List[int]]) -> int:
    """
    convert the graph given to a one in which edge between two vertices are abs diff, then
    cost of a path = path with maximum weight
    such a cost is similar to a cost where cost is sum of weights.
    Now with this cost, we need to find a path with minimum such cost to destination
    One way is by Kruskals MST algorithm
    """
    if not heights:
        return 0
    n = len(heights)
    m = len(heights[0])
    elements = n * m
    edges = get_edges(heights)
    kruskal = Kruskal(elements, edges)
    kruskal.execute()
    # print(kruskal.output)
    max_ans = 0
    for u, v, w in kruskal.output:
        max_ans = max(max_ans, w)
    return max_ans


heights = [[1, 2], [4, 7]]
heights = [[1,2,2],[3,8,2],[5,3,5]]
heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]

print(minimumEffortPath(heights))



