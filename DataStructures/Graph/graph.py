#Implementation 1: Adjacency Matrix
class GraphMatrix:
    def __init__(self,vertices):
        self.V=vertices
        self.graph = [[0] * self.V for _ in range(self.V)]
    
    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1 #remove this if directed graph
     
    def display(self):
        for row in self.graph:
            print(row)

from collections import defaultdict
#Implementation 2: Adjacency List
class GraphList:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, v1, v2):
        if v1 in self.graph.keys() and v2 in self.graph.keys():	#v1&v2 both exist
            self.graph[v1].append(v2) #{v1: [v2]}
            self.graph[v2].append(v1) #{v2: [v1]}
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.graph.keys() and v2 in self.graph.keys():	#v1&v2 both exist
            try:
                self.graph[v1].remove(v2)
                self.graph[v2].remove(v2)
            except ValueError:  #v1 & v2 aren't connected
                pass # do nothing
            return True
        return False 
    
    def add_vertex(self, vertex):
        if vertex not in self.graph.keys(): # If vertex not already in the graph
            self.graph[vertex]=[]
            return True #vertex successfully added
        return False #vertex already present ->not added again
    
    def remove_vertex(self, vertex):
        if vertex in self.graph:
            for other_vertex in self.graph[vertex]: #loop through adjacent vertices
                self.graph[other_vertex].remove(vertex)
                #Before removing a vertex, remove all edges it has with other vertices.
                del self.graph[vertex]
                return True
            return False 

    def display(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex} -> {edges}")

#TEST CASES
my_graph=GraphList()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A','B')
my_graph.add_edge('A','C')
my_graph.add_edge('A','D')
my_graph.add_edge('B','D')
my_graph.add_edge('C','D')

my_graph.remove_vertex('D')

my_graph.display()