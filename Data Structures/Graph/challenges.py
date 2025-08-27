import os 
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
queue_dir = os.path.join(current_dir, '..', "Stack and Queue")
sys.path.append(queue_dir)

from graph import Graph
from Stack import My_Stack
from graph import Graph_
from graph import Graph3
from Queue import MyQueue
import collections

#Challenge : Detect Cycle in a Directed Graph-----------------
#Solution :

'''
This solution performs a depth-first search (DFS) traversal technique, which is well-suited for detecting cycles in a graph. DFS explores as far as possible along each branch before backtracking, making it ideal for uncovering cyclic paths. This unique characteristic of DFS makes it particularly well-suited for detecting cycles, as it inherently traverses through the graph in a manner that allows it to identify repeated nodes.

The essence of this algorithm lies in its ability to systematically explore graphs while keeping track of visited nodes and nodes currently in the recursion stack. This enables the algorithm to efficiently identify cycles by detecting instances where a node is traversed more than once within the same traversal path.'''

#Time complexity : O(V + E) where V is the number of vertices and E is the number of edges.
#Space complexity : O(V) where V is the number of vertices, used for the visited list and recursion stack.
def is_graph_cyclic(graph):
    visited = [False] * graph.vertices #keeps track of whether a node has been visited during the entire algorithm
    rec_stack = [False] * graph.vertices #keeps track of nodes that are part of the current recursive call stack, with FALSE.
    
    for node in range(graph.vertices):
        #Dfs recursion call
        if detect_cycle_rec(graph, node, visited, rec_stack):
            return True
    return False

def detect_cycle_rec(graph, node, visited, rec_stack):
    # Node was already in the recursion stack. Cycle found.
    if rec_stack[node]:
        return True
    
    if visited[node]:
        return False
    
    # Mark current node as visited and add to recursion stack
    visited[node] = True
    rec_stack[node] = True
    head_node = graph.array[node].head_node
    
    while head_node is not None:
        # Pick adjacent node and call it recursively
        adjacent = head_node.data
        # If the node is visited again in the same recursion => Cycle found
        if detect_cycle_rec(graph, adjacent, visited, rec_stack):
            return True
        
        head_node = head_node.next_element
        
    rec_stack[node] = False
    
    return False

g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(3, 0)
g.add_edge(3, 1)

#Challenge : Find a Mother Vertex in a Directed Graph----------------
'''
Statement : Given a directed graph as input, determine a mother vertex within it. A mother vertex in a graph G=(V,E), is vertex V such that all other vertices in G can be reached by a path from V. Although a graph might feature multiple mother vertices, your goal is to identify at least one.
'''

#Solution 1 : 
'''
To find a mother vertex in a given directed graph, we apply a depth-first search (DFS) strategy from each vertex to confirm if there's a vertex from which all other vertices are reachable.We start by iteratively performing a depth-first search (DFS) starting from each vertex in the graph. For each vertex, we call perform_dfs() to see how many vertices can be reached from it. If the number of vertices reached from the current vertex is equal to the total number of vertices in the graph, it means that the current vertex can reach all other vertices and, thus, is a mother vertex. We return this vertex index. If no vertex meets the above condition, we return -1, indicating there's no mother vertex in the graph.
'''
#Time Complexity : O(V(V+E)) because DFS is performed from each vertices.
#Space Complexity : O(V), as in the worst case recursion stack could have all the vertices in the stack.
def find_mother_vertex(graph):
    number_of_vertices_reached = 0
    for i in range(graph.vertices):
        #Perform DFS from each vertex
        number_of_vertices_reached = perform_dfs(graph, i)
        #If all the vertices are reached
        if number_of_vertices_reached == graph.vertices:
            return i
    
    return -1

def perform_dfs(graph, vertex):
    number_of_vertices = graph.vertices
    
    vertices_reached = 0
    
    # Visited vertices tracker
    visited = [False] * number_of_vertices
    
    stack = My_Stack()
    stack.push(vertex)
    
    #Mark source vertex as visited
    visited[vertex] = True
    
    while not stack.is_empty():
        current_vertex = stack.pop()
        
        temp = graph.array[current_vertex].head_node
        
        while temp is not None:
            if not visited[temp.data]:
                stack.push(temp.data)
                # Mark vertex as visited
                visited[temp.data] = True
                vertices_reached += 1
            # Move to next adjacent vertex
            temp = temp.next_element
    
    return vertices_reached + 1  # +1 for the source vertex itself


#Solution 2 : Kosaraju's Strongly Connected Component Algorithm
'''Strongly Connected Component : a group in directed graph in which we can pick any vertices and can reach every other vertices(nodes) in the group.'''
#Time Complexity : O(V+E)
#Space Complexity : O(V) as in the worst case, recursion stack could have all the vertices in stack
def find_mother_vertex_(graph):
    visited = [False] * graph.vertices
    last_v = 0
    for i in range(graph.vertices):
        if not visited[i]:
            perform_DFS(graph, i, visited)
            last_v = i
    
    visited = [False] * graph.vertices
    
    # Verify if last_v is a mother vertex by performing DFS
    perform_DFS(graph, last_v, visited)
    
    # If any vertex is not visited in second pass
    if any(not i for i in visited):
        return -1 # last_v is not a mother vertex
    else:
        return last_v # last_v is a mother vertex
    
def perform_DFS(graph, node, visited):
    visited[node] = True
    
    temp = graph.array[node].head_node
    
    #Traverse all the adjacent vertices
    while temp:
        if not visited[temp.data]:
            # Perform DFS from adjacent vertex
            perform_DFS(graph, temp.data, visited)
        temp = temp.next_element


#Challenge : Count the Number of Edges in an Undirected Graph----------------------
#Solution : 
'''
This approach iterates over each vertex in the graph and calculate the sum of the lengths of Adjacency List corresponding to each vertex. The idea is to count the number of connections or edges in the graph. Dividing the final sum by 2 ensures that each edge is counted only once because, in an undirected graph, each edge is represented twice (once for each vertex it connects). Therefore, dividing by 2 gives the actual count of edges in the graph. This method effectively traverses the adjacency list representation of the graph to determine the total number of edges.
'''
def count_edges(graph):
    sum = 0
    
    for i in range(graph.vertices):
        # add all edge that are linked 
        # to the current vertex 
        sum += len(graph.adj[i])
    
    # The count of edge is always even  
    # because in undirected graph every edge  
    # is connected twice between two vertices 
    return sum // 2


#Challenge : Check If a Path Exists between Two Vertices-----------------------

#Solution : 
'''In this solution, we use the breadth-first search (BFS) approach to determine if a path exists from the source vertex to the destination vertex in a given graph. To do this, we represent the graph using an adjacency list where adjacency[i][j] is 1 if there is an edge between vertex i and vertex j, and 0 otherwise.'''

'''
Benefits of using ""defaultdict(list)"" for graph adjacency lists:
    No KeyError: You don't have to explicitly check if a vertex has been added to the graph before you add an edge from it. You can just adjacency[u].append(v).
    Concise Code: It makes graph construction cleaner and more readable. You avoid if u not in adjacency: adjacency[u] = [] boilerplate.
    Dynamic Vertex Addition: You don't need to know the total number of vertices upfront, nor do they need to be sequential integers. You can use any hashable object (strings, numbers, etc.) as vertex IDs.
'''
# Graph is bidirectional
#Time Complexity : O(V+E) because BFS traverses all the vertices and edges reachable from source vetex
#Space Complexity : O(V+E) This complexity arises from using a dictionary to store all edges, requiring O(E) spaces for E edges and storing up to V nodes in the queue, which also require O(V)

def check_path(edges, source, destination):
    adjacency = collections.defaultdict(list)
    
    for a, b in edges:
        # print("a",a)
        # print("b",b)
        adjacency[a].append(b)
        adjacency[b].append(a)
    
    # print(adjacency)
        
    visited = set()
    queue = [source]
    
    visited.add(source)
    
    while queue:
        current_vertex = queue.pop(0)
        
        #Check if the dequeued vertex is destination
        if current_vertex == destination:
            return True
        
        # Explore neighbors of the current vertex
        for neighbor in adjacency[current_vertex]:
            # If neighbor has not been visited yet, enqueue it and mark it as visited
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    
    # Return False if destination vertex is not reached
    return False

# print(check_path([[0, 1], [1, 2], [1, 3], [1, 4], [3, 5]], 5, 2))


#Challenge : Graph Valid Tree---------------------------

#Solution :
'''To check if the graph is a valid tree, we start from the first node and move to adjacent nodes using a depth-first search. We mark visited nodes and look for cycles by checking if a node has been visited before. If we encounter a previously visited node that is not the parent, we have found a cycle, indicating the graph is not a tree. If the depth-first search started from the first node is complete, but some nodes remain unvisited, the graph is not connected, making it not a tree. If all nodes have been visited and no cycles are found, the graph is a valid tree.'''
def is_tree(graph): 
    visited = [False] * graph.vertices

    # Check cycle by recursively visited adjacent nodes starting from the first node
    if check_cycle(graph, 0, visited, -1):
        return False

    # Check if all nodes were visited from the source
    for i in range(len(visited)):
        if not visited[i]:
            return False
    
    return True


def check_cycle(graph, node, visited, parent):
    visited[node] = True

    # Pick an adjacent node and run recursive DFS
    adjacent = graph.array[node].head_node
    while adjacent:
        if not visited[adjacent.data]:
            if check_cycle(graph, adjacent.data, visited, node):
                return True

        # Check if previously visited node is a parent node
        elif adjacent.data is not parent:
            return True
        adjacent = adjacent.next_element

    return False


g = Graph_(4)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(2,3)
# g.add_edge(3,0)
# print(is_tree(g))

# for i in g.array:
#     print(i.print_list())

#Challenge : Find the Shortest Path between Two Vertices-------------------------
#Solution : 
'''Initialize a visited list with a length equal to the number of nodes in the graph. This list is used to track which nodes have been visited.

Initialize a distance list with a length equal to the number of nodes in the graph. This list is used to record the distance of each node from src node, in terms of the number of edges.

Add src node to an empty queue and mark it as visited in the visited list. Set its distance in the distance list to 0.

While the queue is not empty, perform the following steps:

    Dequeue a node from the queue.

    For each unvisited neighbor of this node, do the following:

    Mark the neighbor as visited in the visited list.

    Add the neighbor to the queue.

    Update the neighbor’s distance in the distance list to be the dequeued node’s distance plus one (this represents one edge away from the dequeued node).

    Continue the process until the queue is empty or the dest node has been visited.

    Return the distance of the dest node from the src node as recorded in the distance list. If the dest node was never visited (indicating no path exists), return -1.
'''
#Time Complexity : O(V+E) This efficiency arises because each vertex is visited exactly once, requiring O(V) time, and each edge is considered, taking O(E) time.
#Space Complexity : O(V)
def find_shorted_path(graph, src, dest):
    if src == dest:
        return 0
    
    result = 0
    
    num_of_vertices = graph.vertices
    
    # A list to hold the history of visited nodes (by default all false)
    visited = [False] * num_of_vertices
    
    # For keeping track of distance of current_node from src
    distance = [0] * num_of_vertices
    
    # Create Queue for Breadth First Traversal and enqueue src in it
    queue = MyQueue()
    queue.enqueue(src)
    visited[src] = True
    
    #Traverse while the queue is not empty
    while not queue.is_empty():
        # Dequeue a node from queue
        current_node = queue.dequeue()
        
        # Visit the neighbor of the dequeued node
        temp = graph.array[current_node].head_node
        
        while temp is not None:
            # Mark the neighbor visited and update its distance from src node
            if not visited[temp.data]:
                queue.enqueue(temp.data)
                visited[temp.data] = True
                distance[temp.data] = distance[current_node] + 1 
                
                # Return the distance when the dest node is visited
                if temp.data == dest:
                    return distance[dest]
            
            temp = temp.next_element
            
    # Return -1 if no path exists between src and dest
    return -1

g = Graph(5)

g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,4) 
g.add_edge(2,4)
g.add_edge(1,4)

# print(find_shorted_path(g, 0, 4))


#Challenge : Remove Edge from a Directed Graph

#Solutions : Time Complexity : O(V), V is number of edges in graph. This is because the function will iterate through the adjacency list.
#Space Complexity : O(1) as no extra space is used.
def remove_edge(graph, source, destination):
    if source in graph.adjacency and destination in graph.adjacency[source]:
        # Remove the destination node from the adjacency list of the source node
        graph.adjacency[source].remove(destination)
    
    return graph.adjacency

g = Graph3(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(1, 3)
print(g.print_adjacency_list())
print(remove_edge(g, 1, 3))