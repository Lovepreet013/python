class Node:
    def __init__(self, data):
        self.data = data
        self.previous_element = None
        self.next_element = None

class Doubly_Linked_List:
    def __init__(self):
        self.head_node = None
        self.tail_node = None
        self.length = 0

    def insert_at_head(self, data):  # Time Complexity: O(1)
        
        if self.length == 0:
            self.tail_node = Node(data)
        
        self.length += 1
        temp_node = Node(data)
        temp_node.next_element = self.head_node
        
        if self.head_node:
            self.head_node.previous_element = temp_node
            self.tail_node = self.head_node if self.tail_node is None else self.tail_node
            
        self.head_node = temp_node
        return self.head_node.data
    
    def insert_at_tail(self, data):  # Time Complexity: O(1)
        if self.length == 0:
            self.head_node = Node(data)
            self.tail_node = self.head_node
            self.length += 1
            return self.tail_node.data
        
        self.length +=1
        temp_node = Node(data)
        self.tail_node.next_element = temp_node
        temp_node.previous_element = self.tail_node
        self.tail_node = temp_node
                
    def delete_at_head(self):
        if self.is_empty():
            print("List is Empty")
            return None

        next_node = self.head_node.next_element
        if next_node:
            next_node.previous_element = None
        self.head_node = next_node
        self.length -= 1
        return self.head_node
    
    def delete_at_tail(self):
        if self.is_empty():
            print("List is Empty")
            return None
        
        if self.head_node == self.tail_node:
            self.head_node = self.tail_node =  None
            self.length = 0
            return None
        
        self.length -= 1
        prev_node = self.tail_node.previous_element
        if prev_node:
            prev_node.next_element = None
        self.tail_node = prev_node
            

    def delete(self, data):
        if self.is_empty():
            print("List is Empty")
            return None

        current_node = self.head_node

        if current_node.data == data:
            return self.delete_at_head()

        # Traverse and search for the node to delete
        while current_node:
            if current_node.data == data:
                prev_node = current_node.previous_element
                next_node = current_node.next_element

                if next_node:
                    prev_node.next_element = next_node
                    next_node.previous_element = prev_node
                else:
                    prev_node.next_element = None
                return True  # Deletion successful
            current_node = current_node.next_element

        print(f"{data} not found in the list.")
        return False  # Data not found

    def is_empty(self):
        return self.head_node is None

    def print_list(self):
        if self.is_empty():
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True


# Testing the corrected doubly linked list
# l = Doubly_Linked_List()
# l.insert_at_head(10)
# l.insert_at_head(1)
# l.insert_at_head(8)
# l.print_list()