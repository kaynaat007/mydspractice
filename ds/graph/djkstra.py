"""
----- Djkstra ------

maintains S & S' as two sets of vertices.
vertices in S are those for which shortest path from source has been found
vertices in S' are those for which we have an estimate ( upper bound on weights ).

we pull a vertex from S' to S with minimum estimate
and then we update the estimates of  all outgoing vertices from this vertex to min ( d[w], d[v] + weight(v, w) )

We repeat this process unless set S' is exhausted.
"""
import heapq
from itertools import count
import math
from priority_q import PQ

MOD = math.pow(10, 9) + 7

class Djkstra:

    def __init__(self):

        self.graph = {}
        self.distances = None

    def execute(self, n, source, graph,  distance, weight):

        pq = PQ()
        for i in range(1, n+1):
            pq.add_task(i, math.inf)

        pq.decrease_priority(source, 0)
        distance[source] = 0

        while not pq.is_empty():

            priority, c, vertex = pq.pop_task()
            for w in graph[vertex]:
                distance[w] = min(distance[w], distance[vertex] + weight[(vertex, w)])
                pq.decrease_priority(w, distance[w])

        return distance

    def main(self, n, edges, source):

        graph = {}
        weight = {}
        distances = [math.inf for i in range(n+1)]
        for i in range(1, n+1):
            graph[i] = set()
        for u, v, w in edges:
            graph[u].add(v)
            graph[v].add(u)
            weight[(u, v)] = w
            weight[(v, u)] = w

        self.graph = graph
        distances = self.execute(n, source, graph, distances, weight)
        self.distances = distances
        # print(distances)


class DFS:

    def __init__(self, graph, n, distances):
        self.graph = graph
        self.vertices = n + 1
        self.visited = [0] * self.vertices
        self.distances = distances
        self.count = 0
        self.is_restricted_path = {}

    def run(self, v, k):

        self.visited[v] = 1
        # print('visited: {}'.format(v))

        if v == self.vertices-1:
            self.is_restricted_path[v] = True
            self.count = (self.count + 1) % MOD

        current_shortest_path_from_source = self.distances[v]
        for i in self.graph[v]:

            if self.visited[i] == 1 and i in self.is_restricted_path:
                self.count = (self.count + 1) % MOD

            if self.visited[i] == 0:  # only if not visited
                if self.distances[i] > current_shortest_path_from_source:
                    self.visited[i] = 1
                else:
                    self.run(i, k)  # visit
                    if i in self.is_restricted_path:
                        self.is_restricted_path[v] = True

    def main(self):

        """
        running DFS
        """
        # print('--- running DFS ----')

        k = 1
        for i in range(1, self.vertices):
            if self.visited[i] == 0:
                self.run(i, k)
                k = k + 1

    def print(self):
        pass

dj = Djkstra()
n = 4
edges = [[0, 1, 2], [1, 2, 4], [2, 3, 3], [3, 0, 5]]
source = 2

edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
n = 5
source = n

edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]
n = 7
source = n




dj.main(n, edges, source)

dfs = DFS(dj.graph, n, dj.distances)
dfs.main()
# print(dfs.is_restricted_path)
print(dfs.count)










