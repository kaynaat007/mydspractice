from typing import List
from collections import deque
import math

import heapq
from itertools import count


REMOVED = '<removed>'

MOD = math.pow(10, 9) + 7


class PQ:

    def __init__(self):
        self.pq = []
        self.entry_finder = {}
        self.counter = count()

    def is_empty(self):

        return len(self.entry_finder.keys()) == 0

    def add_task(self, task, priority):

        if task in self.entry_finder:
            self.remove(task)
        c = next(self.counter)
        element = [priority, c, task]
        self.entry_finder[task] = element
        heapq.heappush(self.pq, element)

    def remove(self, task):

        element = self.entry_finder.pop(task)
        element[-1] = REMOVED

    def pop_task(self):

        while self.pq:
            priority, c, task = heapq.heappop(self.pq)
            if task is REMOVED:
                continue
            del self.entry_finder[task]
            return priority, c, task
        return None, None, None

    def print(self):
        print('---- task in priority from lowest to highest -----')
        while self.pq:
            task = self.pop_task()
            print(task)

    def decrease_priority(self, task, new_priority):

        if task not in self.entry_finder:
            return

        priority, c, task = self.entry_finder[task]
        if task is REMOVED:
            raise Exception('Task deleted')

        if new_priority > priority:
            print('new priority can be only lesser')

        self.remove(task)
        self.add_task(task, new_priority)


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
        print(distances)


class DFS:

    def __init__(self, graph, n, distances):
        self.graph = graph
        self.vertices = n + 1
        self.visited = [0] * self.vertices
        self.distances = distances
        self.restricted_path_count = {}

    def run(self, v, k):

        print('DFS on node {} with path count: {}'.format(v, self.restricted_path_count))

        self.visited[v] = 1
        # print('visited: {}'.format(v))

        if v == self.vertices-1:
            self.restricted_path_count[v] = 1
            return

        count = 0

        current_shortest_path_from_source = self.distances[v]
        for i in self.graph[v]:

            if self.visited[i] == 0 and self.distances[i] < current_shortest_path_from_source: # only if not visited
                self.run(i, k)  # visit
            if i in self.restricted_path_count and self.distances[i] < current_shortest_path_from_source:
                count = (count + self.restricted_path_count[i]) % MOD

        self.restricted_path_count[v] = count

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


def countRestrictedPaths(n: int, edges: List[List[int]]) -> int:
    dj = Djkstra()
    source = n
    dj.main(n, edges, source)
    print(dj.graph)
    dfs = DFS(dj.graph, n, dj.distances)
    dfs.main()
    # print(dfs.is_restricted_path)
    print(dfs.restricted_path_count)
    return int(dfs.restricted_path_count[1])


# n = 7
# edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]

# n = 5
# edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]

# n = 1
# edges = []
#
n = 9
edges = [[6,2,35129],[3,4,99499],[2,7,43547],[8,1,78671],[2,1,66308],[9,6,33462],[5,1,48249],[2,3,44414],[6,7,44602],[1,7,14931],[8,9,38171],[4,5,30827],[3,9,79166],[4,8,93731],[5,9,64068],[7,5,17741],[6,3,76017],[9,4,72244]]

# n = 3
# edges = [[1, 2, 2], [1, 3, 3], [2, 3, 4]]
#
# n = 4
# edges = [[1, 2, 2], [1, 4, 4], [2, 3, 1], [3, 4, 6], [2, 4, 1]]
#
# n = 6
# edges = [[2,4,5],[3,4,2],[2,1,3],[3,1,3],[4,6,5],[5,1,9],[1,4,3],[2,6,5],[5,6,5],[5,3,8],[1,6,6],[3,2,8],[5,2,8]]
print(countRestrictedPaths(n, edges))
