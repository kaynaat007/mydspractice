from ds.atomic_ds.union_find import UnionFind


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
        """
        edges = sorted(self.edges, key=lambda x: x[2])
        uf = UnionFind(self.n)

        for u, v, weight in edges:
            root1 = uf.find(u)
            root2 = uf.find(v)
            if root1 != root2:
                self.output.append((u, v, weight))
                uf.union(root1, root2)


# n = 5
# edges = [(0, 1, 8), (1, 2, 10), (2, 3, 9), (0, 4, 14), (4, 2, 7), (1, 3, 5)]
#
# n = 4
# edges = [(0, 3, 15), (3, 2, 10), (1, 2, 6), (0, 1, 8)]
# kruskal = Kruskal(n, edges)
# kruskal.execute()
# print(kruskal.output)




