from Min_Heap import Min_Heap
from Max_Heap import Max_Heap

#Challenge : Convert Max Heap to Min Heap---------------
#Solution : 
    #Time Complexity : O(n) where n is number of elements in heap.
    #Space Complexity : O(1) because each recursive call is resolved before the next one begins.
def min_heapify(max_heap, index):
    #just apply min_heapify function
    left = (index * 2) + 1
    right = (index * 2) + 2
    
    smallest = index
    
    if len(max_heap) > left and max_heap[smallest] > max_heap[left]:
        smallest = left
    
    if len(max_heap) > right and max_heap[smallest] > max_heap[right]:
        smallest = right
    
    if smallest != index:
        temp = max_heap[smallest]
        max_heap[smallest] = max_heap[index]
        max_heap[index] = temp
        
        min_heapify(max_heap, smallest)
    
    return max_heap

def convert_max(max_heap):
    # Convert the max heap into a min heap using min_heapify starting from the last nonleaf node
    for i in range(len(max_heap) // 2, -1, -1):
        max_heap = min_heapify(max_heap, i)
    
    return max_heap

# print(convert_max([9, 4, 7, 1, -2, 6, 5]))


#Challenge : Find k Smallest Elements in a List---------------------------
'''Statement : Given an unsorted list lst and an integer k, find the k smallest elements from the list using a Heap.'''

#Solution : 
    #Time Complexity : O(k log n) where n is number of elements in heap. This is because populating the Heap takes O(n) time and removing minmium element from Min heap takes O(log n). Because we remove the minimum element k times, the resulting complexity is O(k log n).
    
    #Space Complexity : O(n) because all the elements from the list are stored in Min heap.
def find_k_smallest(lst, k):
    heap = Min_Heap() # Create a min heap
    
    heap.build_heap(lst)
    
    # Create a list of k elements such that:
    # It contains the first k elements from
    # removeMin() function
    k_smallest = [heap.remove_min() for _ in range(k)]
    
    return k_smallest

# print(find_k_smallest([-1, 2, 3, -4, -10], 3))


#Challenge : Find K Largest Elements in the List----------------
#Solution 1:  
    #Time Complexity : O(nlogn + k) where n is list size. This is because the nlogn is the time for sorting and after sorting, selecting the first k elements takes k time.
    
    #Space Complexity : O(n) because sort() in Python takes O(n) space in worst case.
def find_k_largest(nums, k):
    # Sort the list of numbers in descending order
    nums.sort(reverse=True)
    
    # Return the first k elements
    return nums[:k]


#Solution 2: Using Max heap, similar to Min heap solution
    #Time Complexity : O(k log n) where n is number of elements in heap. This is because populating the Heap takes O(n) time and removing max element from heap takes O(log n). Because we remove the max element k times, the resulting complexity is O(k log n).
    
    #Space Complexity : O(n) because all the elements from the list are stored in max heap.
    
def find_k_largest(lst, k):
    heap = Max_Heap() # Create a max heap
    
    heap.build_heap(lst)
    
    # Create a list of k elements such that:
    # It contains the first k elements from
    # remove_max() function
    k_largest = [heap.remove_max() for _ in range(k)]
    
    return k_largest

# print(find_k_largest([-1, 2, 3, -4, -10], 3))