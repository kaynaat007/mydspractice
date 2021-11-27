"""
MST implementation
"""
from ds.atomic_ds.mst_prims import Prim
from typing import List


def get_graph(points):

    edges = []
    n = len(points)
    for i in range(n):
        x1,y1 = points[i]
        for j in range(i+1, n):
            x2,y2 = points[j]
            weight = abs(x1-x2) + abs(y1-y2)
            edges.append((i, j, weight))
    return edges


def find_cost(edges, mst_edge_indexes):
    cost = 0
    for index in mst_edge_indexes:
        cost += edges[index][2]
    return cost


def minCostConnectPoints(points: List[List[int]]) -> int:
    edges = get_graph(points)

    n = len(points)
    source = 0
    weight_function, graph, edge_index = Prim.prepare_graph(edges)

    prim = Prim(weight_function, graph, edges, n)
    prim.mst(source, edge_index)
    return find_cost(edges, prim.output)


points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
points = [[3,12],[-2,5],[-4,1]]
points = [[0,0],[1,1],[1,0],[-1,1]]
points = [[-1000000,-1000000],[1000000,1000000]]
# points = [[0,0]]
print(minCostConnectPoints(points))




