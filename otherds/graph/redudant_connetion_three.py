
class UnionFind:
    """
    Union find solution to detect a cycle and return the edge causing thr cycle in first place
    """

    def __init__(self, n):
        self.n = n
        self.components = [0] * self.n
        for i in range(n):
            self.components[i] = i

    def find(self, u):

        while self.components[u] != u:
            u = self.components[u]
        return u

    def union(self, u, v):

        root1 = self.find(u)
        root2 = self.find(v)

        if root1 != root2:
            self.components[root1] = root2
        else:
            return [u, v]
        return None


def findRedundantConnectionUnionFind(edges):
    uf = UnionFind(2000)
    for u, v in edges:
        ans = uf.union(u, v)
        if ans:
            return ans


edges = [[1,2], [2,3], [3,4], [4,1], [1,5]]

edges = [[1,2], [1,3], [2,3]]

print(findRedundantConnectionUnionFind(edges))
