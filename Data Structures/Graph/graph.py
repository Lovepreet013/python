import os 
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
linked_list_dir = os.path.join(current_dir, '..', "Linked List")
sys.path.append(linked_list_dir)

from linked_list import Linked_List
'''
Graph Terminologies:
    Degree of a Vertex: The total number of edges incident on a vertex. There are two types of degrees:
        In-Degree: The total number of incoming edges of a vertex.
        Out-Degree: The total number of outgoing edges of a vertex.
    Parallel Edges: Two undirected edges are parallel if they have the same end vertices. Two directed edges are parallel if they have the same starting and ending vertices.
    Self Loop: This occurs when an edge starts and ends on the same vertex.
    Adjacency: Two vertices are said to be adjacent if there is an edge connecting them directly.

Types :
    Undirected : the edges have no direction, meaning the connection is bidirectional. There are n(n-1)/2 maximum possible edges in an undirected graph.
    
    Directed : the edges have a direction, meaning the connection is unidirectional. There are n(n-1) maximum possible edges in a directed graph assuming no self loops.

Ways to Represent a Graph:
    Adjacency Matrix : It is 2d matrix where each cell can contain 0 or 1. If it contains 1, there exists an edge between corresponding vertices, eg Matrix[0][1] = 1 shows that an edge exists between vertex 0 and 1.
    
    ""For a directed graph, the usual convention is to think of the rows as sources and the columns as destinations.""
    
    Adjacency List : An array of linked lists is used to store all the edges in the graph. The size of the array is equal to the number of vertices in the graph. Each index of the array contains a vertex. This vertex points to a linked list that contains all the vertices connected to this one.
'''
#Implementation based on adjacency list
class Graph: 
    def __init__(self, vertices):
        #Total no of vertices in the graph
        self.vertices = vertices
        # Defining a list which can hold multiple LinkedLists
        # equal to the number of vertices in the graph
        self.array = []
        # Creating a new LinkedList for each vertex/index of the list
        for _ in range(vertices):
            # Appending a new LinkedList on each array index
            self.array.append(Linked_List())
    
    def add_edge(self, source, destination):
        self.array[source].insert_at_head(destination)
        #If the graph is undirected then we will have to create an edge from the source to the destination and from the destination to the source, making it a bidirectional edge
        #i.e self.array[destination].insert_at_head(source)
    
    def print_graph(self):
        for i in range(self.vertices):
            print(f"Vertex {i}:", end=" ")
            self.array[i].print_list()
            print()

# g = Graph(4) #directed graph
# g.add_edge(0, 2)
# g.add_edge(0, 1)
# g.add_edge(1, 3)
# g.add_edge(2, 3)

# g.print_graph()

class Graph2: #Undirected
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj = [[] for _ in range(vertices)]
    
    def add_edges(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

class Graph_:
    def __init__(self, vertices):
        # Total number of vertices
        self.vertices = vertices
        # definining a list which can hold multiple LinkedLists
        # equal to the number of vertices in the graph
        self.array = []
        # Creating a new Linked List for each vertex/index of the list
        for i in range(vertices):
            self.array.append(Linked_List())

    # Function to add an edge from source to destination
    def add_edge(self, source, destination):
        if source < self.vertices and destination < self.vertices:
        # As we are implementing a directed graph, (1,0) is not equal to (0,1)
            self.array[source].insert_at_head(destination)
            # Uncomment the following line for undirected graph 
            self.array[destination].insert_at_head(source)


class Graph3:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency = {}
 
    def add_edge(self, u, v):
        if u in self.adjacency:
            self.adjacency[u].append(v)
        else:
            self.adjacency[u] = [v]
    
    def print_adjacency_list(self):
        for node, neighbors in self.adjacency.items():
            print(node, "->", neighbors)
'''
Adjacency List : 
    Adding an edge in adjacency lists takes constant time as we only need to insert at the head node of the corresponding vertex.
    Removing an edge takes O(E) time because, in the worst case, all the edges could be at a single vertex and hence, we would have to traverse all E edges to reach the last one.
    Removing a vertex takes O(V + E) time because we have to delete all its edges and then reindex the rest of the list one step back in order to fill the deleted spot.
    Searching an edge between a pair of vertices can take up to O(V) if all V nodes are present at a certain index and we have to traverse them.

Adjacency Matrix :
    Edge operations are performed in constant time as we only need to manipulate the value in the particular cell.
    Vertex operations are performed in O(V^2) since we need to add rows and columns. We will also need to fill all the new cells.
    Searching an edge is O(1) because we can access each edge by indexing.
    
Comparison
Both representations are suitable for different situations. If your application frequently manipulates vertices, the adjacency list is a better choice.
If you are dealing primarily with edges, the adjacency matrix is the more efficient approach
'''

'''
Bipartite Graphs :
The bipartite graph is a special member of the graph family. The vertices of this graph are divided into two disjoint parts in such a way that no two vertices in the same part are adjacent to each other.
In simpler terms, you can split the vertices into two groups, and all the edges go between those two groups, with no edges within the same group. 
The bipartite graph is a type of k-partite graph where k is 2. In a 5-partite graph, we would have 5 disjoint sets and members of a set would not be adjacent to each other.

--> All the acyclic graphs can be bi-partite, but in the case of cyclic graphs, they must contain an even number of vertices.

Types : 
Star Graph
Acyclic Graph
Path Graph
'''