''''
Djsktra implementation
'''

import math
from ds.atomic_ds.priority_q import PQ

MOD = math.pow(10, 9) + 7

import heapq
from itertools import count


REMOVED = '<removed>'


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


dj = Djkstra()
n = 4
edges = [[0, 1, 2], [1, 2, 4], [2, 3, 3], [3, 0, 5]]
source = 2

