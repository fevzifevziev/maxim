"""
1. Написать методы в классе Graph для вычисления порядка и размера графа """
class Graph:
    def __init__(self,graph_dict = None):
        if graph_dict == None:
            self.graph_dict = {}
        self.graph_dict = graph_dict

    def graph_order(self):
        return len(self.graph_dict.keys())

    def graph_size(self):
        edges = []
        for vertex in self.graph_dict:
            for n in self.graph_dict[vertex]:
                if (vertex, n) not in edges:
                    edges.append((vertex, n))
        return int(len(edges)/2)


g_raph = {'A':["C"],
     'B':["C", "E"],
     'C':["A", "B", "D", "E"],
     'D':["C"],
     'E':["C", "B"],
     'F':[]}

graph = Graph(g_raph)
print("Порядок графа = ",graph.graph_order())
print("Размер графа = ",graph.graph_size())
