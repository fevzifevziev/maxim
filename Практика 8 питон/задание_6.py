"""8.6. Пусть заданы две вершины i и j написать метод для вывода всех путей из вершины i в вершину j"""
class Graph:
    def __init__(self,graph_dict = None):
        if graph_dict == None:
            self.graph_dict = {}
        self.graph_dict = graph_dict

    def find_all_paths(self, i, j, path = []):
        path = path + [i]
        if i == j:
            return [path]
        if not i in self.graph_dict:
             return []
        paths = []
        for node in self.graph_dict[i]:
            if node not in path:
                newpaths = self.find_all_paths(node, j, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

g_raph = {'A':["C","G"],
     'B':["C", "E"],
     'C':["A", "B", "D", "E"],
     'D':["C"],
     'E':["C", "B"],
     'F':["F"],
     'G':["G", "A"],
     'H':[]}

graph = Graph(g_raph)
print("Вывод всех путей из вершины i в вершину j",graph.find_all_paths("A","B"))
print("-"*30)
print(graph.graph_dict)
