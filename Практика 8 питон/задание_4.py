"""8.4. В классе Graph добавить метод добавления ребра в граф и метод удаления ребра из графа"""
class Graph:
    def __init__(self,graph_dict = None):
        if graph_dict == None:
            self.graph_dict = {}
        self.graph_dict = graph_dict

    def edge_append(self, vertex, adjacent_vertex):
        if (vertex in self.graph_dict.keys()) and (adjacent_vertex in self.graph_dict.keys()) :
            if adjacent_vertex not in self.graph_dict[vertex]:
                self.graph_dict[vertex].append(adjacent_vertex)
            if vertex not in self.graph_dict[adjacent_vertex]:
                self.graph_dict[adjacent_vertex].append(vertex)
        else:
            print("вершины не существует !")

    def edge_delete(self, vertex, adjacent_vertex): # A C
        if (vertex in self.graph_dict.keys()) and (adjacent_vertex in self.graph_dict.keys()) :
            if adjacent_vertex in self.graph_dict[vertex]:
                del self.graph_dict[vertex][self.graph_dict[vertex].index(adjacent_vertex)] # удоление элимента списко по его первому вхождению
            if vertex in self.graph_dict[adjacent_vertex]:
                del self.graph_dict[adjacent_vertex][self.graph_dict[adjacent_vertex].index(vertex)] # удоление элимента списко по его первому вхождению
        else:
            print("вершины не существует !")


g_raph = {'A':["C","G"],
     'B':["C", "E"],
     'C':["A", "B", "D", "E"],
     'D':["C"],
     'E':["C", "B"],
     'F':["F"],
     'G':["G", "A"],
     'H':[]}

graph = Graph(g_raph)
#graph.edge_append(input("1я вершина - ") , input("2я вершина - ") )
graph.edge_delete(input("1я вершина - ") , input("2я вершина - ") )
print("-"*30)
print(graph.graph_dict)
