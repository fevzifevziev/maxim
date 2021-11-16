"""8.7. В классе Graph написать метод для вычисления плотности графа"""
class Graph:
    def __init__(self,graph_dict = None):
        if graph_dict == None:
            self.graph_dict = {}
        self.graph_dict = graph_dict

    def graph_size(self):
        edges = []
        for vertex in self.graph_dict:
            for n in self.graph_dict[vertex]:
                if (vertex, n) not in edges:
                    edges.append((vertex, n))
        return int(len(edges)/2)

    def density(self):
        l = self.graph_size()
        g = len(self.graph_dict.keys())
        return 2 * l / (g ** 2 - g)


g_raph = {'A':["C","G"],
     'B':["C", "E"],
     'C':["A", "B", "D", "E"],
     'D':["C"],
     'E':["C", "B"],
     'F':["F"],
     'G':["G", "A"],
     'H':[]}

graph = Graph(g_raph)
print("плотность графа",graph.density())
print("-"*30)
print(graph.graph_dict)
