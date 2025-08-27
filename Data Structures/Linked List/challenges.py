from linked_list import Linked_List, Node
from doubly_linked_list import Doubly_Linked_List

#Challenge 1 : Insertion at tail without using tail_node-----------------

#Solution : Time Complexity : O(n) where n is the number of nodes in the linked list, Space Complexity : O(1)
def insert_at_tail(head, value): #head of linked list at input and the value to be inserted
    new_node = Node(value)
    
    if head is None:
        head = new_node
        return head
    
    current = head
    
    #Iterate over the linked list
    while current.next_element:
        current = current.next_element
    
    #Append the new node at the end
    current.next_element = new_node
    return head.data

#Challenge : Search in singly linked list-------------------

#Solution : Time Complexity : O(n), Space Complexity : O(1)
def search(head, value):
    current = head
    while current:
        if current.data == value:
            return True
        current = current.next_element
    return False


#Challenge : Delete function in singly linked list-------------------

#Solution : Time Complexity : O(n), Space Complexity : O(1)
def delete(head, value):
    if head is None:
        print("Empty List")
        return head
    
    if head.data == value:
        return head.next_element
    
    current = head
    
    while current.next_element:
        if current.next_element.data == value:
            current.next_element = current.next_element.next_element
            return True
    
        current = current.next_element
        
    print(f"{value} not found in the list.")
    return head

#Challenge : Length of linked list-------------------
def length(head):
    count = 0
    current = head
    
    if current is None:
        return count
    
    while current:
        count += 1
        current = current.next_element
    
    return count

#Challenge : Reverse a linked list-------------------
#Solution : 
'''
To reverse the linked list, we will follow these steps:

    Initialize three pointers: previous, next_node, and current. The previous and next_node pointers are initialized as NULL, while the current pointer is initialized to the head of the linked list.

    Iterate over the linked list. While iterating, perform the following steps:

        Before changing the next pointer of current, store the next node in next_node to prevent losing the reference to the rest of the list.
        
        Update the next pointer of current to point to the previous node. This effectively reverses the pointer of the current node.
        
        Move previous to current and current to next_node to move to the next iteration.
        
        After reversing the whole linked list, we’ll change the head pointer to the previous pointer because previous will be pointing to the new head node.
'''

def reverse(head):
    # To reverse a linked list, we need to keep track of three things
    previous_node = None
    current_node = head
    next_node = None

    while current_node:
        next_node = current_node.next_element 
        current_node.next_element = previous_node
        previous_node = current_node
        current_node = next_node

    # After the loop, previous_node will be the new head of the reversed linked list
    return previous_node


# l = Linked_List()
# l.insert_at_head(10)
# l.insert_at_head(9)
# l.insert_at_head(8)
# l.insert_at_head(7)

# print("Original List:")
# l.print_list()

# l.head_node = reverse(l.head_node)  # assign the new head

# print("Reversed List:")
# l.print_list()

#Challenge : Linked List Cycle-------------------------------
'''Given the head of a linked list, check whether or not a cycle is present in the linked list. A cycle is present in a linked list if at least one node can be reached again by traversing the next pointer. If a cycle exists, return TRUE; otherwise, return FALSE.'''

#Solution : Floyd’s cycle-finding algorithm to detect a cycle in the linked list

'''
Initialize two pointers, p1 and p2, to point to the head of the linked list.
Traverse the linked list until the end of the linked list is reached.
While traversing the linked list, move p1 one node at a time and move p2 two nodes at a time.
    If at any point the two pointers meet, it means that a cycle has been found. In this case, we return TRUE.
If the end of the linked list is reached, that is, p2 is pointing to NULL, a cycle does not exist. In this case, we return FALSE.
'''
#Time Complextiy : if cycle does not exist, O(n) where n is the number of nodes in the linked list; if cycle exists, O(n + k) where k is the number of nodes in the cycle. Space Complexity : O(1)
def check_cycle(head):
    # Initialize two pointers to point to the head of the linked list
    slow = head
    fast = head
    
    # Traverse the linked list until the end of the linked list is reached
    while slow and fast and fast.next_element:
        slow = slow.next_element  # Move slow pointer one node at a time
        fast = fast.next_element.next_element # Move fast pointer two nodes at a time
        
        # If slow and fast meet at the same node, a cycle is found
        if slow == fast:
            return True
        
    # If the end of the linked list is reached, no cycle exists
    return False
        
# # Create a linked list
# ll = Linked_List()
# ll.insert_at_head(10)
# ll.insert_at_head(20)
# ll.insert_at_head(30)

# # Print the list
# print("Testing with a normal linked list (no cycle):")
# ll.print_list()

# # Test for cycle - should return False
# print("Cycle Detected:" if check_cycle(ll.head_node) else "No Cycle Detected")

# # Now, create a cycle manually
# # Get reference to nodes
# first_node = ll.head_node              # 30
# second_node = ll.head_node.next_element  # 20
# third_node = second_node.next_element    # 10

# # Create a cycle: last node (10) points back to second node (20)
# third_node.next_element = second_node

# print("\nTesting with a cycle introduced manually:")
# # Test for cycle - should return True
# print("Cycle Detected:" if check_cycle(ll.head_node) else "No Cycle Detected")


#Challenge : Middle of the Linked List-------------------
#Solution 1 : Brute Force Approach, Time Complexity : O(n), Space Complexity : O(1)
def find_mid(head):
    node = head 
    mid = 0
    
    mid = length(head) // 2 + 1
    
    for i in range(mid - 1):
        node = node.next_element
    
    return node.data

def length(head):
    # Start from the first element
    curr = head
    length = 0
    
    #Traverse the linked list
    while curr is not None:
        length += 1
        curr = curr.next_element
        
    return length

#Solution 2 : Two pointers
'''We can use two pointers to solve this problem with constant space complexity. The mid pointer traverses the linked list one step at a time, while the fast pointer takes two steps at a time. This makes the fast pointer reach the end of the linked list in n/2 iterations, and the mid pointer, by this time, reaches the middle of the linked list.'''
#Time Complextiy : O(n), Space Complexity : O(1)
def find_mid_(head):
    mid_node = head
    fast_pointer = head
    
    # Move mid_node (slower) one step at a time and fast_pointer (faster) two steps at a time
    while fast_pointer and fast_pointer.next_element:
        mid_node = mid_node.next_element
        fast_pointer = fast_pointer.next_element.next_element
        
    return mid_node.data


#Challenge : Remove Duplicates from a Linked List--------------------------

#Solution : Time complexity is O(n^2) as for each value we are checking if it is already present in the list, Space Complexity : O(n) for storing the unique values in a list
def remove_duplicate(head):    
    if head is None:
        return head
    
    ref_list = []
    current = head
    prev = None  # To keep track of the previous node
    
    while current:
        if current.data not in ref_list:
            ref_list.append(current.data)
            prev = current
        else:
            # If the data is already in the ref_list, delete the node
            prev.next_element = current.next_element    
                
        current = current.next_element
    
    return head

#Improved Solution : Time Complexity : O(n), Space Complexity : O(n) for storing the unique values in a set
def remove_duplicate_using_set(head):
    if head is None :
        return head
    
    seen = set()
    current = head
    prev = None
    
    while current:
        if current.data not in seen:
            seen.add(current.data)
            prev = current
        else:
            # If the data is already in the seen set, delete the node
            prev.next_element = current.next_element

        current = current.next_element
    
    return head

#Challenge : Union and Intersection of Linked Lists--------------------
'''
Given the heads of two linked lists, head1 and head2, as inputs. Implement the union and intersection functions for the linked lists. The order of elements in the output lists doesn’t matter.

Here’s how you will implement the functions:

    Union: This function will take two linked lists as input and return a new linked list containing all the unique elements.

    Intersection: This function will take two linked lists as input and return all the common elements between them as a new linked list.
'''

#Solution :
#Time Complexity : O(n), Space Complexity : O(n) for storing the unique values in a set
def union(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    # Join the two linked lists
    current = head1
    
    while current:
        current = current.next_element
        
        if current.next_element is None:
            current.next_element = head2
            break
    
    #Remove duplicates
    remove_duplicate_using_set(head1)

#Solution : Time Complexity : O(n + m) where n is number of elements in linked list 1 and m is number of elements in linked list 2, Space Complexity : O(n) for storing the unique values in a set
def intersection(head1, head2):
    if head1 is None or head2 is None:
        return None
    
    # Create a set to store the elements of the first linked list
    seen_in_head1 = set()
    
    # New List
    result = Linked_List()
    
    #Traverse the first linked list
    current1 = head1 
    while current1:
        if current1.data not in seen_in_head1:
            seen_in_head1.add(current1.data)
        current1 = current1.next_element
    
    # Traverse the second linked list and check for intersection
    current2 = head2
    while current2:
        if current2.data in seen_in_head1:
            result.insert_at_head(current2.data)
    
        current2 = current2.next_element

    return result


l = Linked_List()
l.insert_at_head(10)
l.insert_at_head(9)
l.insert_at_head(8)
l.insert_at_head(7)
l.insert_at_head(7)
l.insert_at_head(4)
l.insert_at_head(3)
l.insert_at_head(15)

l1 = Linked_List()
l1.insert_at_head(1)
l1.insert_at_head(1)
l1.insert_at_head(15)
l1.insert_at_head(2)
l1.insert_at_head(3)
l1.insert_at_head(4)
l1.insert_at_head(7)

# union(l.head_node, l1.head_node)
# l.print_list()
# intersection_result = intersection(l.head_node, l1.head_node)

# print("Intersection Result : ")
# intersection_result.print_list()


#Challenge : Return the Nth Node from End---------------------------
'''Given the head of a linked list, return the nth node from the end of the linked list.'''

#Solution : Time Complexity : O(n), Space Complexity : O(1)
def find_nth(head, n):
    result = head # This iterator will reach the Nth node
    end = head # This iterator will reach the end of the list
    
    count = 0
    
    while count < n:
        end = end.next_element
        count += 1
    
    while end is not None:
        end = end.next_element
        result = result.next_element
    
    return result.data

l = Linked_List()        
l.insert_at_head(10)
l.insert_at_head(9)
l.insert_at_head(8)
l.insert_at_head(7)

result = find_nth(l.head_node, 4)
# print(result)

#Challenge : Find If a Doubly Linked List Is a Palindrome-----------------
#Solution : Time Complexity : O(n), Space Complexity : O(1)
def is_palindrome(head):
    start = head
    end = get_tail_node(head)
    
    #if the list is empty, it is palindrome
    if start is None:
        return True
    
    #Otherwise we traverse the list from both ends
    while start != end and start.previous_element != end:
        # If data mismatches at any point, list is not a palindrome
        if start.data != end.data:
            return False
        
        start = start.next_element
        end = end.previous_element
    
    return True  # If we reach here, the list is a palindrome

def get_tail_node(head):
    temp = head
    
    while temp.next_element is not None:
        temp = temp.next_element
    return temp  # Return the last node (tail node) of the linked list

d_list = Doubly_Linked_List()
d_list.insert_at_head(1)
d_list.insert_at_head(2)
d_list.insert_at_head(2)
d_list.insert_at_head(1)

print(is_palindrome(d_list.head_node))