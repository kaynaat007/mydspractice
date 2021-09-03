"""
First code converts a 2D matrix where each cell has some value to a set of edges and their weights
weight of an edge(u, v) is abs difference between heights[u] - heights[v]

Second function converts an a dict of edges to adjacency graph
"""

from collections import defaultdict


def get_edges(heights):

    n = len(heights)
    m = len(heights[0])
    elements = n * m
    edges = {}
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
                edges[(k, upper_vertex)] = abs(upper_val - current_val)
            if left_vertex is not None and left_vertex >= 0:
                left_val = heights[i][j - 1]
                edges[(k, left_vertex)] = abs(left_val - current_val)

            if right_vertex is not None and right_vertex <= elements - 1:
                right_val = heights[i][j + 1]
                edges[(k, right_vertex)] = abs(right_val - current_val)

            if down_vertex <= elements - 1:
                down_val = heights[i + 1][j]
                edges[(k, down_vertex)] = abs(down_val - current_val)

            k += 1
    return edges


def edges_to_graph(edges):
    """
    edges to graph
    """
    graph = defaultdict(list)
    for key, val in edges.items():
        u, v = key
        graph[u].append(v)
    return graph
