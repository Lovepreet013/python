class Max_Heap:
    def __init__(self):
        self.heap = []
    
    def insert(self, val): #Time Complexity : O(log n)
        self.heap.append(val)
        self.__percolate_up( len(self.heap) - 1) #This function will swap the values at parent-child nodes until the heap property is restored.
    
    def get_max(self): #Time Complexity : O(1)
        if self.heap:
            return self.heap[0]
        return None
    
    #This function removes and returns the maximum value in the heap. It first checks if the length of the heap is greater than 1, if it is, it saves the maximum value in a variable, swaps the maximum value with the last leaf, deletes the last leaf, and restores the max heap property on the rest of the tree by calling the __max_heapify()
    def remove_max(self): #Time Complexity : O(log n)
        if len(self.heap) > 1:
            max = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.__max_heapify(0)
            return max
            
        elif len(self.heap) == 1:
            max = self.heap[0]
            return max
        
        else:
            return None
    
    #The two underscores before the functions imply that these functions should be treated as private functions although there is no actual way to enforce class function privacy in Python.
    
    #This function restores the heap property by swapping the value at a parent node if it is less than the value at a child node. After swapping, the function is called recursively on each parent node until the root is reached.
    def __percolate_up(self, index): #Time Complexity : O(log n)
        parent = (index-1)//2
        if index <= 0:
            return 
        
        elif self.heap[parent] < self.heap[index]:
            tmp = self.heap[parent]
            self.heap[parent] =  self.heap[index]
            self.heap[index] = tmp
            self.__percolate_up(parent)
    
    #This function restores the heap property after a node is removed. It swaps the values of the parent nodes with the values of their largest child nodes until the heap property is restored
    def __max_heapify(self, index):  #Time Complexity : O(log n)
        left = (index * 2) + 1
        right = (index * 2) + 2
        
        largest = index
        
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        
        if largest != index:
            tmp = self.heap[largest]
            self.heap[largest] = self.heap[index]
            self.heap[index] = tmp
            self.__max_heapify(largest)
    
    
    def build_heap(self, arr): #Time Complexity : O(n)
        self.heap = arr
        
        for i in range(len(arr) - 1, -1, -1 ):
            self.__max_heapify(i)

# heap = Max_Heap()
# heap.insert(12)
# heap.insert(10)
# heap.insert(-10)
# heap.insert(100)

# print(heap.heap)