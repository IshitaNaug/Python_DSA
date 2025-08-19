class Graph:
    def __init__(self, Vno):
        self.vertex_count = Vno
        self.adj_list = {i: [] for i in range(Vno)}  

    def add_edge(self, u, v, weight=1):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_list[u].append((v, weight))
            self.adj_list[v].append((u, weight))   
        else:
            print("Invalid vertex")

    def remove_edge(self, u, v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            for edge in self.adj_list[u]:
                if edge[0] == v:
                    self.adj_list[u].remove(edge)
                    break
            for edge in self.adj_list[v]:
                if edge[0] == u:
                    self.adj_list[v].remove(edge)
                    break
        else:
            print("Invalid vertex")

    def has_edge(self, u, v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            for edge in self.adj_list[u]:
                if edge[0] == v:
                    return True
            return False
        else:
            print("Invalid vertex")
            return False

    def print_adj_list(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])
            
            
#Driver Code
g = Graph(4)
g.add_edge(0, 1, 5)
g.add_edge(2, 3, 7)
g.add_edge(1, 2, 3)

g.print_adj_list()            