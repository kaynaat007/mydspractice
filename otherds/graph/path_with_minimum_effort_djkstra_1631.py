from typing import List
import heapq
from itertools import count
import math


REMOVED = '<removed>'

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

        if task in self.entry_finder:
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
        for i in range(n):
            pq.add_task(i, math.inf)

        pq.decrease_priority(source, 0)
        distance[source] = 0

        while not pq.is_empty():

            priority, c, vertex = pq.pop_task()
            for w in graph[vertex]:
                distance[w] = min(distance[w], max(distance[vertex], weight[(vertex, w)]))
                pq.decrease_priority(w, distance[w])

        return distance

    def main(self, n, edges, source):

        graph = {}
        weight = {}
        distances = [math.inf for i in range(n)]
        for i in range(n):
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
    """

    n = len(heights)
    m = len(heights[0])
    elements = n * m
    edges = get_edges(heights)
    dj = Djkstra()
    dj.main(elements, edges, 0)
    print(dj.distances)
    return dj.distances[-1]


heights = [[1, 2], [4, 7]]
heights = [[1,2,2],[3,8,2],[5,3,5]]
heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
print(minimumEffortPath(heights))






