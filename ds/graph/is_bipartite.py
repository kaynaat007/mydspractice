
from collections import deque
import math

class Graph:

    def __init__(self, V):
        self.vertices = V
        self.graph = {v: set() for v in range(V)}

    def init(self, *input):

        for i, e in enumerate(input):
            for v in e:
                self.add_edge(i, v)

    def get_adjacent(self, u):

        return self.graph[u]

    def add_edge(self, source_vertex, target_vertex):

        self.graph[source_vertex].add(target_vertex)

    def print(self):

        for v, edges in self.graph.items():
            print('edged connected to vertex : {} are {}'.format(v, edges))

class BFS:

    def __init__(self, graph, components, val):

        self.graph = graph
        self.pie = [-1] * graph.vertices
        self.distance = [math.inf] * graph.vertices
        self.color = [0] * graph.vertices
        self.WHITE = 0
        self.GRAY = 1
        self.BLACK = 2
        self.components = components
        self.val = val

    def run(self, source):

        self.color[source] = self.GRAY
        self.pie[source] = -1
        self.distance[source] = 0

        q = deque([source])

        while q:
            u = q.popleft()
            for v in self.graph.get_adjacent(u):
                if self.color[v] == self.WHITE:
                    self.color[v] = self.GRAY
                    self.pie[v] = u
                    self.distance[v] = self.distance[u] + 1
                    self.components[v] = self.val
                    q.append(v)
                if self.distance[v] != math.inf and self.distance[u] == self.distance[v]:
                    return False

            self.color[u] = self.BLACK
        return True

    def get_color_name(self, code):

        if code == 0:
            return 'WHITE'
        if code == 1:
            return  'GRAY'
        if code == 2:
            return 'BLACK'

    def details(self):

        for u in range(self.graph.vertices):
            print('color: {} is {}'.format(u, self.get_color_name(self.color[u])))
            print('parent: {} is {}'.format(u, self.pie[u]))
            print('distance from source: {} is {}'.format(u, self.distance[u]))
            print('-----------------')


array = [[1,3], [0,2], [1,3], [0,2]]

array = [[1,2,3], [0,2], [0,1,3], [0,2]]


array =  [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]

# array = [[1,3],[0,2],[1,3],[0,2]]

# array = [[1,2,3], [0,2], [0,1,3], [0,2]]


def is_bipartite(array):

    g = Graph(len(array))
    n = len(array)
    g.init(*array)

    components = [0 for i in range(n)]

    val = 0

    for u in range(len(array)):
        val = val + 1
        if components[u] == 0:
            components[u] = val
            bfs = BFS(g, components, val)
            v = bfs.run(u)
            if not v:
                return False
    return True

print(is_bipartite(array))
