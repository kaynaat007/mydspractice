from ds.atomic_ds.priority_q import PQ
from collections import defaultdict

class Prim:

    def __init__(self, weight, graph, edges, n):
        self.weight = weight
        self.graph = graph
        self.output = []
        self.S = [0 for _ in range(n)]
        self.edges = edges

    @staticmethod
    def prepare_graph(edges):
        weight_function = {}
        graph = defaultdict(list)
        edge_index = {}
        for i, edge in enumerate(edges):
            u, v, weight = edge
            graph[u].append(v)
            graph[v].append(u)
            weight_function[(u, v)] = weight
            weight_function[(v, u)] = weight
            edge_index[(u, v)] = i
            edge_index[(v, u)] = i

        return weight_function, graph, edge_index


    def mst(self, s, edge_index):
        """
        initialize set S as zero for all vertices
        initialize MST as empty
        for all v in adj[s], put edge (s, v) in heap
        while heap is not empty,
            - pick minimum edge (u, w) from heap
            - add it to MST set
            - take it's vertex which is not in S . say w
            - put all adj edges (w, x) edges in heap such that x is not in S.
            - if x is in  S, delete it from heap
            - add w to set S
        """
        pq = PQ()
        for v in self.graph[s]:
            index = edge_index[(s, v)]
            edge = (s, v)
            pq.add_task(index, self.weight[edge])

        self.S[s] = 1

        while not pq.is_empty():
            priority, counter, task = pq.pop_task()
            self.output.append(task)
            u, v, weight = self.edges[task]
            if self.S[u] == 0:
                w = u
            else:
                w = v
            for adjacent_vertex in self.graph[w]:
                current_edge_index = edge_index[(w, adjacent_vertex)]
                current_edge = (w, adjacent_vertex)
                if self.S[adjacent_vertex] == 0:  # adjacent vertex in S', we must add edge to heap
                    pq.add_task(current_edge_index, self.weight[current_edge])
                else:  # else adjacent_vertex in S.  # vertex is in proper set, we need to remove the edge
                    pq.remove(current_edge_index)

            self.S[w] = 1
        for index in self.output:
            print(self.edges[index])
        print('MST done..')


# edges = [(0, 1, 8), (1, 2, 10), (2, 3, 9), (0, 4, 14), (4, 2, 7), (1, 3, 5)]
# n = 5
# source = 0
# weight_function, graph, edge_index = Prim.prepare_graph(edges)
#
# print('weight function: {}'.format(weight_function))
# print('graph: {}'.format(graph))
# print('edge index: {}'.format(edge_index))
# prim = Prim(weight_function, graph, edges, n)
# prim.mst(source, edge_index)
# print('output: {}'.format(prim.output))



