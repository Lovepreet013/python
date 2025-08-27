class Node:
    def __init__(self, data):
        self.data = data #value 
        self.next_element = None #node pointing to the next node

class Linked_List:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    # Time Complexity : O(1) 
    def insert_at_head(self, data):
        # Create a new node containing your specified value
        temp_node = Node(data)
        # The new node points to the same node as the head
        temp_node.next_element = self.head_node
        
        self.tail_node = temp_node if self.tail_node is None else self.tail_node
        
        self.head_node = temp_node  # Make the head point to the new node
        return self.head_node  # return the new list
    
    # Time Complexity : O(1)
    def delete_at_head(self): 
        if self.is_empty():
            print("List is Empty")
            return None
        
        self.head_node = self.head_node.next_element
        return self.head_node

    def is_empty(self):
        if self.head_node is None:
            return True
        else:
            return False

    # Supplementary print function
    def print_list(self):
        if(self.is_empty()):
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
