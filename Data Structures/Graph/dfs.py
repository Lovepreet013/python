import os 
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
queue_dir = os.path.join(current_dir, '..', "Stack and Queue")
sys.path.append(queue_dir)

from graph import Graph
from Stack import My_Stack

#Graph Traversal Algorithms:--------------------
'''Take any vertex as the starting point. This is the lowest level in your search. The next level consists of all the vertices adjacent to the starting vertex. A level higher would mean the vertices adjacent to the nodes at the lower level.'''

#Depth First traversal (DFS):-----------------
'''
The DFS algorithm is the opposite of BFS in the sense that it grows depth-wise.
Starting from any node, we keep moving to an adjacent node until we reach the farthest level. Then we move back to the starting point and pick another adjacent node. Once again, we probe to the farthest level and move back. This process continues until all nodes are visited.
'''
#Time complexity : O(V + E)
#Space complexity : O(V) for the visited list and stack used in DFS traversal.
def dfs_traversal(graph, source):
    result = []
    num_of_vertices = graph.vertices
    visited = [False] * num_of_vertices
    
    #Create a stack for dfs
    stack = My_Stack()
    
    # Push the source vertex and mark it as visited
    stack.push(source)
    visited[source] = True
    
    # Perform DFS
    while not stack.is_empty():
        # Pop a vertex from the stack and add it to the result
        current_vertex = stack.pop()
        result.append(current_vertex)
        
        # Push all neighbors of the popped vertex
        temp = graph.array[current_vertex].head_node
        while temp is not None:
            if not visited[temp.data]:
                stack.push(temp.data)
                # Mark the neighbors as visited when they are pushed
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
# print("Graph Traversal using DFS:", dfs_traversal(g, 0))