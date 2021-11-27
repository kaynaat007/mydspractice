"""
back edge
cross edge
forward edge
Tree edge
"""
from collections import defaultdict

from typing import List


class DFS:
    """
    Graph is adjacency List
    """

    def __init__(self, graph, v):
        self.graph = graph
        self.vertices = v

        self.visited = [0] * self.vertices
        self.time = 0
        self.arr = [0] * self.vertices
        self.dep = [0] * self.vertices
        self.cc = [0] * self.vertices
        self.cycle = False

    def run(self, v, k, stack):

        if self.cycle:
            return

        self.time += 1
        self.arr[v] = self.time
        self.visited[v] = 1
        self.cc[v] = k
        stack[v] = True  # this node is in stack

        # explore neighbours one by one. If we encounter any neighouring node which is already in stack, this means
        # we have back EDGE.
        for i in self.graph[v]:
                if self.visited[i] == 0:  # if vertex i is not visited
                    self.run(i, k, stack)
                else:  # if vertex i is already visited
                    if i in stack and stack[i]:
                        self.cycle = True
                        return
        stack[v] = False
        self.time += 1
        self.dep[v] = self.time

    def main(self):

        k = 1
        stack = {}
        for i in range(self.vertices):
            if self.visited[i] == 0:
                if self.cycle:
                    return True
                self.run(i, k, stack)
                k = k + 1

    def is_cycle(self):

        self.main()
        return self.cycle


def convert_into_adjaceny_list(edges):

    graph = defaultdict(list)
    for edge in edges:
        graph[edge[1]].append(edge[0])
    return graph


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:

    graph = convert_into_adjaceny_list(prerequisites)
    dfs = DFS(graph, numCourses)
    return not dfs.is_cycle()


numCourses = 2
prerequisites = [[1,0],[0,1]]

# numCourses = 2
# prerequisites = [[1,0]]


numCourses = 2
prerequisites = [[0,1]]


print(canFinish(numCourses, prerequisites))