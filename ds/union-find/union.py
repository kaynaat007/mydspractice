"""
Union Find
Union by rank
node will smallerr size points to node with higher size.

"""


class UnionFind:


    def __init__(self, data):
        self.data = data
        self.n = len(self.data)
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


# data = [4, 5, 1, 3]
# u = UnionFind(data)
#
# u.union(0, 1)
# print(u.components())
#
# u.union(1, 2)
# print(u.components())
# # u.union(1, 2)
# # print(u.components())


