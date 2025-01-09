# Graph
- [ ]  Adjacency Matrix
- [ ]  Adjacency List
- [ ]  add_vertex() / remove_vertex()
- [ ]  add_edge() / remove_edge()
- [ ]  Big O 
## 1. Graph Terminology
- **Graph (G)**: G(V,E) -> **Vertices (V):** Points/nodes, **Edges (E):** Connections btw nodes 

- **Directed/Undirected Graph:** Directed:edges have a direction - e.g.webpages, Twitter follows). Undirected: edges are ordered pairs (e.g.FB friendships).
- **Weighted/Unweighted Graph:** Whether edges have associated weights/costs (e.g. Weighted:distance btw cities)
- **Cyclic/Acyclic:** A cyclic graph contains a path from at least one node back to itself

- **Degree:** The number of edges connected to a vertex.
    - **In/Out-degree:** Number of incoming/outgoing edges to a vertex (for directed graphs).
      
- **Path:** A sequence of vertices connected by edges.
    - **Simple Path:** A path that does not repeat any vertices.
    - **Cycle:** A path that starts and ends at the same vertex.
 
- **Connected Graph:** An undirected graph where there is a path between every pair of vertices.
    - **Strongly Connected:** In a directed graph, every vertex is reachable from every other vertex.
    - **Weakly Connected:** In a directed graph, the graph is connected if we ignore the direction of edges.
      
- **Tree:** A connected, acyclic (no cycles) undirected graph.
- A binary tree is a type of graph with a limitation that a node can point to max 2 other nodes
    - So, LL is a form of a tree. A tree is a form of a graph
- **Bipartite Graph:** A graph that can be divided into two disjoint sets where every edge connects a vertex in one set to a vertex in the other set.
- Graphs can be **traversed** (we travel to all the nodes and do stuff) - check traversal algorithms
  

## 2 Ways to Represent Graphs:
- **Adjacency Matrix:** A 2D array (matrix) of binary values indicating whether any 2 nodes are connected. The element at (i, j) is 1 (or the weight) if there is an edge from vertex i to vertex j, otherwise 0. → ➖:large memory complexity
- **Adjacency List:** A list or hash table where key=a vertex, its value=list of its adjacent vertices → ➖: No quick way to determine whether a given edge is present in the graph


**Choosing Between Adjacency Matrix and Adjacency List:**
| Adjacency Matrix    | Adjacency List |
| --------            | -------        |
| Suitable for dense graphs with many edges.  | Suitable for sparse graphs with few edges (consumes less memory)  |
| Requires 𝑂(𝑉^2) space, where 𝑉=number of vertices  |Requires 𝑂(𝑉+𝐸) space, where 𝐸=number of edges. Space-efficient for sparse graphs.Efficient for iterating over all edges.|
| ➕ Fast look-up for edge existence (O(1) time). |Accessing neighbors of a vertex is faster. |


### 1-Adjacency Matrix
- **Pros:** Fast look-up for edge existence (O(1) time)
- **Cons:** Space complexity is O(V^2), inefficient for large sparse graphs. Inefficient for iterating over all edges.
- If weighted edges, store weights instead of 1s
- <img width="347" alt="image" src="https://github.com/user-attachments/assets/077a4732-b681-440c-973e-07a76b038c90">
- You'll have a 45 degree line of 0s ->A vertex can't point back to itself
- If you have a bidirectional graph, you will have a mirrored image around the 45-degree line

```
class GraphMatrix:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * self.V for _ in range(self.V)]

    def add_edge(self, u, v):
        self.graph[u][v] = 1 
        self.graph[v][u] = 1 # Remove this line if the graph is directed

    def display(self):
        for row in self.graph:
            print(row)
```

### 2- Adjacency List (preferred)
- Represent the graph as a dictionary
- key=origin vertex, value=[vertices it has edges with]
- **Pros:** Space-efficient for sparse graphs.Efficient for iterating over all edges.
- **Cons:** Checking if an edge exists between two vertices can take O(V) time in the worst case. Slightly more complex to implement than an adjacency matrix.
<img width="347" alt="image" src="https://github.com/user-attachments/assets/d3e0e968-a19d-4d20-bfd0-bc578b93d546">

```
from collections import defaultdict
class GraphList:
    def __init__(self): #create an empty dict
        self.graph = defaultdict(list) #can also do self.graph={}

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Remove this line if the graph is directed

    def display(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex} -> {edges}")
```

## Big O
### Time Complexity
<img width="647" alt="image" src="https://github.com/user-attachments/assets/5cbd1912-e1d9-4a24-ae5d-a6448939fe09">

- In a typical graph, traversal time complexity is O(V+E)


### Space Complexity
Big difference btw adjacency list &matrix: In A.M. each vertex also needs to store the vertices it’s not connected to 
<img width="390" alt="image" src="https://github.com/user-attachments/assets/8c77df7f-7aa5-4bc8-839b-6d17aad39d5f">


Binary Tree
- A binary tree is a type of graph with a limitation that a node can point to max 2 other nodes
- So, LL is a form of a tree. A tree is a form of a graph
