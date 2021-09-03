

class Graph:

    def __init__(self, V):
        self.vertices = V
        self.graph = {v: set() for v in range(V)}

    def init(self, *input):

        for i, e in enumerate(input):
            for v in e:
                self.add_edge(i, v)

    def get_adjacent(self, u):

        return self.graph[u]

    def add_edge(self, source_vertex, target_vertex):

        self.graph[source_vertex].add(target_vertex)

    def print(self):

        for v, edges in self.graph.items():
            print('edged connected to vertex : {} are {}'.format(v, edges))






