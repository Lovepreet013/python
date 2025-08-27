import os 
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
linked_list_dir = os.path.join(current_dir, '..', "Linked List")
queue_dir = os.path.join(current_dir, '..', "Stack and Queue")
sys.path.append(linked_list_dir)
sys.path.append(queue_dir)

from graph import Graph
from Queue import MyQueue

#Graph Traversal Algorithms:--------------------
'''Take any vertex as the starting point. This is the lowest level in your search. The next level consists of all the vertices adjacent to the starting vertex. A level higher would mean the vertices adjacent to the nodes at the lower level.'''

#Breadth First Search (BFS):---------------
'''
The BFS algorithm earns its name because it grows breadth-wise. All the nodes at a certain level are traversed before moving on to the next level.
The level-wise expansion ensures that for any starting vertex, you can reach all others, one level at a time.
'''
#Time Complexity : O(V + E) where V is the number of vertices and E is the number of edges.
#Space Complexity : O(V) for the visited list and queue used in BFS traversal.
def bfs_traversal(graph, source):
    result = []
    num_of_vertices = graph.vertices
    visited = [False] * num_of_vertices
    
    #Create a queue for BFS
    queue = MyQueue()
    
    # Enqueue the source vertex and mark it as visited
    queue.enqueue(source)
    visited[source] = True
    
    #Perform BFS
    while not queue.is_empty():
        # dequeue a vertex from the queue and add it to the result
        current_vertex = queue.dequeue()
        result.append(current_vertex)
        
        # Enqueue all neighbors of the dequeued vertex
        temp = graph.array[current_vertex].head_node
        while temp is not None:
            if not visited[temp.data]:
                queue.enqueue(temp.data)
                # Mark the neighbors as visited when they are enqueued
                visited[temp.data] = True
            temp = temp.next_element
    
    return result
    
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(4, 3)
g.add_edge(3, 2)
g.add_edge(1, 2)
g.add_edge(1, 5)

# print("Graph Traversal using BFS:", bfs_traversal(g, 0))