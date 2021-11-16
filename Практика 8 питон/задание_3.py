""" 3. В классе Graph добавить метод добавления вершины в граф, метод удаления вершины из графа """
class Graph:
    def __init__(self,graph_dict = None):
        if graph_dict == None:
            self.graph_dict = {}
        self.graph_dict = graph_dict

    def add_vertices_to_the_graph(self):
        while True:
            vertice = input("Введите новую вершину графа: ")
            if vertice in self.graph_dict.keys():
                print ("Такая вершина уже существует\n",'-'*26)
            else:
                Graph.func_a_v_t_t_g(self, vertice)
                break

    def remove_vertices_in_a_graph(self):
        while True:
            vertice = input("Удалить вершину графа: ")
            if vertice in self.graph_dict.keys():
                Graph.func_r_v_i_a_g(self, vertice)
                break
            else:
                print ("Такой вершины не существует\n",'-'*26)

    def func_r_v_i_a_g(self, name):
        del self.graph_dict[name]
        for vertex in self.graph_dict:
            if name in self.graph_dict.get(vertex):
                i = -1
                for l in self.graph_dict.get(vertex):
                    i += 1
                    if l == name:
                        del self.graph_dict.get(vertex)[i]

    def func_a_v_t_t_g(self, name):
        self.graph_dict[name] = []

        while True:
            peremen = False
            question = input('Добавить смежную вершину для вершины "{}"  ? (Y - да) - '.format(name))
            if question == "Y":
                vert = input("Введите смежную вершину: ")
                for l in list(self.graph_dict.values()):
                    if vert in l :
                        peremen = True
                if vert == name:
                    peremen = True
                if peremen == True:
                    if len(self.graph_dict.get(name)) == 0:        #из-за ошибки вследствие несуществования последнего элимента списка
                        self.graph_dict.get(name).append(vert)
                    else:
                        if vert not in self.graph_dict.get(name)[-1]:
                            self.graph_dict.get(name).append(vert)
                else:
                    print("Такой вершены не существует в графе!")
            else:
                break
        print(self.graph_dict.get(name))
        for gdgn in self.graph_dict.get(name):
            if gdgn != name:
                self.graph_dict.get(gdgn).append(name)


g_raph = {'A':["C","G"],
     'B':["C", "E"],
     'C':["A", "B", "D", "E"],
     'D':["C"],
     'E':["C", "B"],
     'F':["F"],
     'G':["G", "A"],
     'H':[]}

graph = Graph(g_raph)
graph.add_vertices_to_the_graph()
#graph.remove_vertices_in_a_graph()
print("-"*30)
print(graph.graph_dict)
