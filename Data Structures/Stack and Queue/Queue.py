import sys
import os

#1. Get the current directory of queue.py
# __file__ is a special variable that holds the path to the current script.
# os.path.abspath(__file__) converts it to an absolute path (e.g., C:\...\queue.py).
# os.path.dirname(...) gets the directory part (e.g., C:\...\Stack and Queue).
current_dir = os.path.dirname(os.path.abspath(__file__))

#sys.path is a list of strings, where each string is a directory path. When Python needs to import a module, it iterates through these paths, looking for a file matching the module name 

# 2. Construct the path to the 'Linked List' directory
# We need to go up one level from 'Stack and Queue' (to 'Data Structures')
# and then down into 'Linked List'.
# '..' means "go up one directory"
# os.path.join handles path separators correctly for different operating systems (/, \)
linked_list_dir = os.path.join(current_dir, '..', "Linked List")

# 3. Add the 'Linked List' directory to sys.path
# This is the crucial step! We're adding the calculated directory to Python's search path.
sys.path.append(linked_list_dir)

from doubly_linked_list import Doubly_Linked_List

class My_Queue:
    def __init__(self):
        self.items = Doubly_Linked_List()
    
    def is_empty(self):
        return self.items.length == 0
    
    def front(self):
        if self.is_empty():
            return None
        return self.items.head_node.data
    
    def back(self):
        if self.is_empty():
            return None
        return self.items.tail_node.data
    
    def enqueue(self, value):
        return self.items.insert_at_tail(value)
    
    def dequeue(self):
        return self.items.delete_at_head()
    
    def print_list(self):
        return self.items.__str__()
    
    def size(self):
        return self.items.length

my_queue_obj = My_Queue()
my_queue_obj.enqueue(1)
my_queue_obj.enqueue(2)
my_queue_obj.enqueue(3)
my_queue_obj.enqueue(4)
# print(my_queue_obj.dequeue())
# print(my_queue_obj.size())


#Another way to implement queue
class MyQueue:
    def __init__(self):
        self.queue_list = []
        self.queue_size = 0

    def is_empty(self):
        return self.queue_size == 0

    def front(self):
        if self.is_empty():
            return None
        return self.queue_list[0]

    def rear(self):
        if self.is_empty():
            return None
        return self.queue_list[-1]

    def size(self):
        return self.queue_size
    
    def enqueue(self, value):
        self.queue_size += 1
        self.queue_list.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        front = self.front()
        self.queue_list.remove(self.front())
        self.queue_size -= 1
        return front