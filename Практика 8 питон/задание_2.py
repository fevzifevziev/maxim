""" 2. Написать методы в классе Graph для поиска изолированных вершин и вершин с петлями и вывести их количество """
class Graph:
    def __init__(self,graph_dict = None):
        if graph_dict == None:
            self.graph_dict = {}
        self.graph_dict = graph_dict

    def vertices_with_loops(self):
        a = []
        for vertice in self.graph_dict:
            for vertice_2 in self.graph_dict.get(vertice):
                if vertice == vertice_2:
                    a += [vertice]
        return a

    def number_of_vertices_with_loops(self):
        return len(Graph.vertices_with_loops(self))

    def find_isolated_vertices(self):
        isolated = []
        for vertex in self.graph_dict:
            if not self.graph_dict[vertex]:
                isolated += [vertex]
        return isolated


g_raph = {'A':["C","G"],
     'B':["C", "E"],
     'C':["A", "B", "D", "E"],
     'D':["C"],
     'E':["C", "B"],
     'F':["F"],
     'G':["G", "A"],
     'H':[]}

graph = Graph(g_raph)
print("изолированные вершины -", graph.find_isolated_vertices())
print("Вершины с петлями -", graph.vertices_with_loops())
print("Количество вершин с петлями =", graph.number_of_vertices_with_loops())
