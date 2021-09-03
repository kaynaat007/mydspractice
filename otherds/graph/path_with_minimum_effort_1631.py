from typing import List
from collections import defaultdict
import math


def edges_to_graph(edges):

    graph = defaultdict(list)
    for key, val in edges.items():
        u, v = key
        graph[u].append(v)
    return graph


def dfs(graph, edges, v,  visited, target, ans, threshold):

    if target == v:
        ans[0] = True
        return

    visited[v] = True

    for u in graph[v]:
        if not visited[u] and edges[(v, u)] <= threshold:
            dfs(graph, edges,  u, visited, target, ans, threshold)


def dfs_main(edges, graph, n, threshold):

    visited = [False for _ in range(n)]
    visited[0] = True
    target = n-1
    ans = [False]
    i = 0
    dfs(graph, edges, i,  visited, target, ans, threshold)
    return ans[0]


def minimumEffortPath( heights: List[List[int]]) -> int:
    """
    binary search the answer
    And each possible value will be checked through a DFS.
    log(max_possible_value_in_edge) * O(edges)
    """

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

            if j == m-1:
                right_vertex = None
            else:
                right_vertex = k + 1

            down_vertex = k + m

            if upper_vertex >= 0:
                upper_val = heights[i-1][j]
                edges[(k, upper_vertex)] = abs(upper_val - current_val)
            if left_vertex is not None and left_vertex >= 0:
                left_val = heights[i][j-1]
                edges[(k, left_vertex)] = abs(left_val - current_val)

            if right_vertex is not None and right_vertex <= elements - 1:
                right_val = heights[i][j+1]
                edges[(k, right_vertex)] = abs(right_val - current_val)

            if down_vertex <= elements-1:
                down_val = heights[i+1][j]
                edges[(k, down_vertex)] = abs(down_val - current_val)

            k += 1

    graph = edges_to_graph(edges)
    max_edge_value = max(edges.values())
    low = 0
    high = max_edge_value
    best_answer = math.inf
    while low <= high:
        mid = low + (high - low) // 2
        # print('checking mid: {}'.format(mid))
        ans = dfs_main(edges, graph, elements, mid)
        if ans:
            best_answer = min(best_answer, mid)
            high = mid - 1
        else:
            low = mid + 1

    return best_answer





heights = [[1, 2, 8]]
heights = [[1], [2], [8]]
heights = [[1, 2], [4, 7]]
heights = [[1,2,2],[3,8,2],[5,3,5]]
heights = [[1,2,3],[3,8,4],[5,3,5]]
heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
print(minimumEffortPath(heights))






