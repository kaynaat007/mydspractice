from typing import List
from atomic_ds.mst_kruskal import Kruskal


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


def minCostConnectPoints(points: List[List[int]]) -> int:
    edges = get_graph(points)
    n = len(points)
    kruskal = Kruskal(n, edges)
    kruskal.execute()
    cost = 0
    for _, _, w in kruskal.output:
        cost += w
    return cost


points = [[0,0],[2,2],[3,10],[5,2],[7,0]]

points = [[3,12],[-2,5],[-4,1]]
points = [[0,0],[1,1],[1,0],[-1,1]]
points = [[-1000000,-1000000],[1000000,1000000]]
points = [[0,0]]
print(minCostConnectPoints(points))




