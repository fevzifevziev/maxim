"""8.5. В классе Graph добавить метод определения степени вершины, метод вывода вершины с максимальной (минимальной) степенью."""
class Graph:
    def __init__(self,graph_dict = None):
        if graph_dict == None:
            self.graph_dict = {}
        self.graph_dict = graph_dict

    def vertex_power(self, vertex):
        if vertex in self.graph_dict.keys():
            return len(self.graph_dict[vertex])
        else:
            return None

    def vertex_power_min(self):
        len_min_vertex_power = 0
        min_vertex_power = ""
        for vertex in self.graph_dict.keys():
            if len_min_vertex_power < len(self.graph_dict[vertex]):
                len_min_vertex_power = len(self.graph_dict[vertex])
                min_vertex_power = vertex
        return min_vertex_power, len_min_vertex_power

    def vertex_power_max(self):
        len_max_vertex_power = 0
        max_vertex_power = ""
        for vertex in self.graph_dict.keys():
            if len(self.graph_dict[vertex]) == 0:
                max_vertex_power = vertex
            if len_max_vertex_power > len(self.graph_dict[vertex]):
                len_max_vertex_power = len(self.graph_dict[vertex])
                max_vertex_power = vertex
        return max_vertex_power, len_max_vertex_power

g_raph = {'A':["C","G"],
     'B':["C", "E"],
     'C':["A", "B", "D", "E"],
     'D':["C"],
     'E':["C", "B"],
     'F':["F"],
     'G':["G", "A"],
     'H':[]}

graph = Graph(g_raph)
print("Cтепень вершины = ",graph.vertex_power(input("определение степени вершины - ")))
print("вершина с максимальной степенью",graph.vertex_power_min())
print("вершина с минимальной степенью",graph.vertex_power_max())
print("-"*30)
print(graph.graph_dict)
