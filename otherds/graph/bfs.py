"""
A graph search algorithm on G(V, E) where V is set of vertices and E set of edges.

BFS proceeds to maintain three color of vertices. white, gray and black. white vertices are not visited. gray vertices
are what currently in queue and black vertices are done with.

BFS produces called predeccesor graph. A set of vertices Vp of predecessor graph consists of all vertices of graph s
such that pie(v) is not NULL union {source}.
while edges set E contain EDGES of form  (pie(v), v ) where pie(v) is the parent of v through which v was visited. This graph
is actually  a tree and its a spanning tree.

BFS produces shortest distance of each vertex from source S.

BFS produces a christmas tree like structure where it divides the vertices into certain level numbers. First all vertices
at level 1, then all vertices at level 2, etc. The last level is the height of this tree.

 An edge cannot cross a certain level for eg it cannot happen that there is an edge from level 1 to level 3 why ?
because if there was such an edge, then vertex in level 3 wouldn't be there. it would have been discovered earlier only
while we were exploring vertices at level 1.

if there is an edge between vertices of same level, then G is not bipartite why ? because it will lead to a cycle of
odd length and if a G has a cycle of odd length, it cannot be bipartite.


"""
from collections import deque
import math
from ds.graph.graph_adt import Graph


class BFS:

    def __init__(self, graph):

        self.graph = graph
        self.pie = [-1] * graph.vertices
        self.distance = [math.inf] * graph.vertices
        self.color = [0] * graph.vertices
        self.WHITE = 0
        self.GRAY = 1
        self.BLACK = 2

    def run(self, source):

        print('running BFS..')

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
                    q.append(v)

            self.color[u] = self.BLACK

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
g = Graph(len(array))
g.init(*array)
bfs = BFS(g)
bfs.run(0)
bfs.details()




