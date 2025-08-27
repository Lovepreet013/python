from Queue import MyQueue
from stack import My_Stack

#Challenge 1 : Generate Binary Numbers From 1 to n Using a Queue-----------------
#Solution : Time Complexity : O(n), Space Complexity : O(n)
def binary_nums(n):
    result = []
    queue = MyQueue()
    
    #Start with '1' in queue
    queue.enqueue(1)
    
    #Loop to generate binary numbers up to n
    for i in range(n):
        #Dequeue the front element 
        result.append(str(queue.dequeue()))
        
        # Generate new binary numbers by appending '0' and '1' to the dequeued number
        s1 = result[i] + '0'
        s2 = result[i] + '1'
        
        # Enqueue the new binary numbers back into the queue
        queue.enqueue(s1)
        queue.enqueue(s2)
    
    return result

#Challenge : Implement Two Stacks Using One List ------------------------------------
#Note: Perform all operations in-place without resizing the underlying list, maintaining a fixed size throughout.

#Solution : Time Complexity : O(1) for push and pop operations, Space Complexity : O(n) for the list
class Two_Stack:
    def __init__(self, size):
        self.size = size
        self.stack_list = [None] * size
        self.top1 = -1
        self.top2 = size
        
    def push1(self, value):
        # Increment top pointer and add element to stack 1 if space is available, else print stack overflow and exit
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.stack_list[self.top1] = value
        else:
            print("Stack Overflow")
            exit(1)
    
    def push2(self, value):
        # Decrement top pointer and add element to stack 2 if space is available, else print stack overflow and exit
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.stack_list[self.top2] = value
        else:
            print("Stack Overflow")
            exit(1)
    
    def pop1(self):
        # Return and remove top element from stack 1 if not empty, else print stack underflow and exit
        if self.top1 >= 0:
            value = self.stack_list[self.top1]
            self.top1 -= 1
            return value
        else:
            print("Stack Underflow")
            exit(1)
    
    def pop2(self):
        # Return and remove top element from stack 2 if not empty, else print stack underflow and exit
        if self.top2 < self.size:
            value = self.stack_list[self.top2]
            self.top2 += 1
            return value
        else:
            print("Stack Underflow")
            exit(1)
    
    def peek1(self):
        # Return top element of stack 1 without removing it if not empty, else print stack underflow and exit
        if self.top1 >= 0:
            return self.stack_list[self.top1]
        else:
            print("Stack Underflow")
            exit(1)
    
    def peek2(self):
        # Return top element of stack 2 without removing it if not empty, else print stack underflow and exit
        if self.top2 < self.size:
            return self.stack_list[self.top2]
        else:
            print("Stack Underflow")
            exit(1)

#Challenge : Reverse First k Elements of Queue------------------
#Solution : Time Complexity : O(n), Space Complexity : O(k) as we use stack to store k elements to be reversed
def reverse_k_elements(queue, k):
    #Handling invalid input
    if queue.is_empty() is True or k > queue.size() or k <= 0:
        return None
    
    stack = My_Stack()
    for _ in range(k):
        stack.push(queue.dequeue())
    
    while stack.is_empty() is False:
        queue.enqueue(stack.pop())
    
    size = queue.size()
    
    for _ in range(size - k):
        queue.enqueue(queue.dequeue())
    
    return queue

#Challenge: Implement Queue Using Stacks-----------------------
#Solution 1: Queue with efficient dequeue()
'''
Here are the detailed steps of this solution:
    Initialize two stacks, main_stack and temp_stack, with empty lists.
    enqueue(): Whenever a new value is to be inserted, we pop all values from main_stack and push them into temp_stack so that the new value is pushed to the bottom of main_stack. We then pop the elements from temp_stack and push them back into main_stack, preserving the FIFO order.
    dequeue(): Since the order of insertion was preserved during enqueue(), we simply pop from the top of main_stack.
'''
class New_Queue:
    def __init__(self):
        self.main_stack = My_Stack()
        self.temp_stack = My_Stack()
    
    # Inserts element in the queue
    def enqueue(self, value): #Time Complexity : O(n) because we transfer all the elements to main_stack and back, Space Complexity : O(n)
        # Push the value into main_stack in O(1)
        if self.main_stack.is_empty() and self.temp_stack.is_empty():
            self.main_stack.push(value)
        else:
            while not self.main_stack.is_empty():
                self.temp_stack.push(self.main_stack.pop())
            #Inseting the values in queue
            self.main_stack.push(value)
            
            while not self.temp_stack.is_empty():
                self.main_stack.push(self.temp_stack.pop())
                
    # Removes element from queue
    def dequeue(self): #Time Complexity : O(1) for pop operation, Space Complexity : O(1) as we are not using any extra space
        #if stack is empty then return None
        if self.main_stack.is_empty():
            return None
        
        value = self.main_stack.pop()
        return value

#Solution 2: Queue with efficient enqueue()
#In this solution, we make the dequeue() operation more expensive by transferring all the values from the main stack to the temporary stack.
class New_Queue2:
    def __init__(self):
        self.main_stack = My_Stack()
        self.temp_stack = My_Stack()
        
    def enqueue(self, value): #Time Complexity : O(1), Space Complexity : O(n) as we use 2 stacks
        # Push the value into main_stack in O(1)
        self.main_stack.push(value)
    
    #If temp_stack is empty, transfer all elements from main_stack to temp_stack so Time Compelxity : O(n)
    #If temp_stack is not empty, just pop from temp_stack in O(1)
    #Space Complexity : O(1) because no extra space is used
    def dequeue(self):
        if self.main_stack.is_empty() and self.temp_stack.is_empty():
            return None
        
        if not self.temp_stack.is_empty():
            front = self.temp_stack.pop()
            return front
        
        # Transfer all elements to temp_stack
        while not self.main_stack.is_empty():
            self.temp_stack.push(self.main_stack.pop())
            
        # Pop the first value. This is the oldest element in the queue
        front = self.temp_stack.pop()
        return front
        

#Challenge : Sort values in stack--------------------
#Solution : Time Complexity O(n^2) because each of the n elements in the input stack may require up to n operations (push, pop) on both the main stack and the temporary stack., Space Complexity O(n) as we use a second stack to sort the values
"""
1. Use a second temp_stack.
2. Pop value from mainStack and store it.
3. If the value is greater or equal to the top of temp_stack,
  then push the value in temp_stack
  else pop all values from temp_stack
      and push them in mainStack
      and in the end push value in temp_stack
4. Repeat from step 2 till the mainStack is not empty.
5. When mainStack will be empty,
    temp_stack will have sorted values in descending order.
6. Now transfer values from temp_stack to mainStack
    to make values sorted in ascending order.
"""
def sort_stack(stack):
    temp_stack = My_Stack()
    
    while not stack.is_empty():
        value = stack.pop()
        
        # If value is not none and larger, push it at the top of the temp_stack
        if temp_stack.peek() is not None and value >= temp_stack.peek():
            temp_stack.push(value)
        else:
            while not temp_stack.is_empty() and value < temp_stack.peek():
                stack.push(temp_stack.pop())
                
            # Place value as the smallest element in temp_stack
            temp_stack.push(value)
            
    # Transfer from temp_stack => stack
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())
        
    return stack


#Solution 2 : Recursive Approach
#Time Complexity : O(n^2) because each element might require both a recursive call and an insertion, resulting in the possibility of numerous recursive calls and insertions for every element.
#Space Complexity : O(n) due to recursive calls.
'''
The steps of the algorithm are given below:
Start with an input stack.
Check if the stack is not empty.
Recursively pop the element of the stack and store it until the stack is empty.
Recursively sort the remaining stack.
Insert the stored element back into the stack. While inserting the stored element back into the stack, follow these steps:
    Compare the stored element with the top element of the stack.
    If the stored element is smaller than the top element, push it onto the stack.
    If the stored element is larger than the top element:
    Recursively pop the top elements of the stack until the top element is smaller than the stored element, and store this top element temporarily.
    Insert the stored element into the stack.
    push the temporarily stored elements back onto the stack.
Return the sorted stack.'''
def sort_stack_recursive(stack):
    if not stack.is_empty():
        # Pop the top element off the stack
        value = stack.pop()
        # Sort the remaining stack recursively
        sort_stack_recursive(stack)
        # Push the top element back into the sorted stack
        insert(stack, value)
    
    return stack


def insert(stack, value): #helper function
    if stack.is_empty() or value < stack.peek():
        stack.push(value)
    else:
        temp = stack.pop()
        insert(stack, value)
        stack.push(temp)

#Challenge : Evaluate Postfix Expression Using a Stack-------------------
#Solution : Time Complexity : O(n) because we traverse the exp once, where n is the number of characters in exp, Space Complexity : O(n) as we use a stack to store the operands

def apply_operator(op, num1, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 // num2  # Assuming integer division for simplicity

def evalutate_postfix(exp):
    stack = My_Stack()
    
    for char in exp:
        if char.isdigit():
            #push number in stack
            stack.push(int(char))
        else:
            # Operator encountered
            # Pop top two numbers from stack
            right = stack.pop()
            left = stack.pop()
            
            # Apply operator to operands and push result back to stack
            result = apply_operator(char, left, right)
            stack.push(result)
    
    #Final result is at the top of stack
    return stack.pop()

# print(evalutate_postfix("921*-8-4+"))

#Challenge : Next Greater Element Using a Stack------------------
'''
Implement a next_greater_element() function that takes a list of integers, lst, as input and returns the next greater number for every element in the list.
The next greater number for a number lst[i] is the first number to its right that is greater than lst[i]. If no such number exists, return -1 for this number.
'''

#Solution : 
'''
The steps of the algorithm are given below:
Start by initializing an empty stack and a result list, res, with the same length as the input list lst. This list will store the next greater elements for each element in lst.
Initially, populate it with -1 to indicate that no next greater element has been found yet.
Then, iterate over the input list, lst, in reverse order (from the last element to the first).
For each element lst[i], enter a while loop.

Continue the loop until the stack is not empty and the current element lst[i] is greater than or equal to the top element of the stack.
    Within the while loop, pop elements from the stack using stack.pop() as long as the condition holds TRUE. This step ensures that we remove elements from the stack that cannot be the next greater element for any element to the right, including the current element lst[i].
    After the while loop, check if the stack is not empty; this means that the top element of the stack is the next greater element for the current element lst[i]. Therefore, update the corresponding index in the result list, res, with the value of the top element of the stack.
After handling the current element, push it onto the stack to ensure that for subsequent elements to the left, they can find the next greater element in the stack.
After the iteration, return the result list res, which contains the next greater elements for each element in the input list lst.'''

#The Python built-in function "reversed()" is used to obtain a reversed iterator for a given sequence. This means it doesn't create a new reversed list or modify the original sequence in place. Instead, it provides an efficient way to iterate over the elements in reverse order.

def next_greater_element(lst):
    stack = My_Stack()
    res = [-1] * len(lst)  # Initialize result list with -1
    
    for i in reversed(range(len(lst))):
        # While stack has elements and the current element is greater 
        # than top element, pop all elements
        while not stack.is_empty() and stack.peek() <= lst[i]:
            stack.pop()
        
        # If the stack has an element, the top element will be 
        # greater than ith element
        if not stack.is_empty():
            res[i] = stack.peek()
        stack.push(lst[i])
    
    return res

# print(next_greater_element([7, 9, 8, 3, 4, 5]))

#Challenge : Find the Celebrity-----------------
'''In a gathering of N individuals (labeled from 0 to N-1), there's a possibility of one person being a celebrity. A celebrity is characterized by being known by everyone else and not knowing any attendees. This scenario is represented using an N X N binary matrix, where each cell contains either a 0 or a 1. If matrix[i][j] = 1, signifies that a person ith knows person jth.
For a give matrix, determine the existence of a celebrity within a group. If a celebrity is indetified, return its label, otherwise return -1. 
'''

#Solution : 
'''Before we delve into the solution, it's crucial to consider the minimum and maximum number of celebrities that can exist within the given matrix.

To explore the possibility of having more than one celebrity, consider two individuals, X and Y, both purported to be celebrities. Following the celebrity criteria:
 1. X, being the celebrity, should not know Y, which implies matrix[X][Y] = 0. Consequently, Y should know X, or matrix[Y][X] = 1.
 2. Y, being the celebrity, should not know X, which implies matrix[Y][X] = 0. Consequently, X should know Y, or matrix[X][Y] = 1.

These conditions contradict each other, as they suggest that X should both know and not know Y simultaneously, which is impossible. Thus, the assumption of having more than one celebrity contradicts the definition of a celebrity in this context. Therefore, the maximum number of celebrities possible in a matrix is 1.
Let's walk through the steps of the solution:

We create a stack to hold the indexes of all attendees, treating everyone as a potential celebrity initially.

We populate the stack with every attendee's index, starting from 0 up to (N - 1).

We determine potential celebrities by repeatedly popping two indexes from the stack to compare two individuals at a time.

    For the popped individuals, we check whether one knows the other by referencing the binary matrix, where a value of 1 at (i,j) indicates that person i knows person j.
    If individual x knows individual y, x cannot be a celebrity; y is considered a potential celebrity and is pushed back into the stack.
    Otherwise, x does not know person y, y is eliminated from consideration, and x is pushed back into the stack for further comparison.
    Continue the process until only one index(individual) remains in the stack. This index represents the tentative celebrity.  

Next, to verify the celebrity status, we ensure that the tentative celebrity does not know any of the other attendees (no outgoing acquaintance) while every other attendee knows them (incoming acquaintance from all).

    We check the binary matrix for the following conditions for the tentative celebrity index:
        The row corresponding to the tentative celebrity should have all zeros (except for the diagonal element), indicating they know no one. We do not need to check the diagonal element here.
        The column corresponding to the tentative celebrity should have all ones (except for the diagonal element), indicating everyone knows them. We do not need to check the diagonal element here.
Finally, if the tentative celebrity meets the verification criteria, their index is returned as the confirmed celebrity. Otherwise, we return -1, signifying the absence of a celebrity.'''

#Time Complexity : O(n) where n is length of the matrix, representing the number of individuals. This results from the stack potentially growing to a height of O(N) and the verification step involving traversal of only one row and one column for the potential celebrity.
#Space Complexity : O(n) because we are using a stack with maximum height of N, where n is the length of the matrix, representing the number of individuals
def knows(matrix, x, y):
    # Returns True if x knows y, else returns False
    return matrix[x][y] == 1

def find_celebrity(matrix):
    stack = My_Stack()
    celebrity = -1
    
    n = len(matrix[0])  # Ensure n is the size of the matrix
    
    for i in range(n):
        stack.push(i)
    
    while not stack.is_empty():
        x = stack.pop()
        
        if stack.is_empty():
            celebrity = x
            break
        
        y = stack.pop()
        
        if knows(matrix, x, y):
            # x knows y, discard x and push y back in stack
            stack.push(y)
        else:
            # y is discarded, x is pushed back
            stack.push(x)
    
    #Verify the potential celebrity
    for j in range(n):
        # A celebrity knows no one, and everyone knows the celebrity
        if celebrity != j and (knows(matrix, celebrity, j) or not knows(matrix, j, celebrity)):
            return -1
    
    return celebrity

# print(find_celebrity([[0, 1, 0, 0],
#                       [0, 0, 0, 0],
#                       [0, 1, 0, 0],
#                       [0, 1, 0, 0]]))



#Challenge : Valid Parentheses--------------------
'''Given a string, exp, which may consist of opening and closing parentheses. Your task is to check whether or not the string contains valid parenthesization.

The conditions to validate are as follows:

Every opening parenthesis should be closed by the same kind of parenthesis. Therefore, {) and [(]) strings are invalid.

Every opening parenthesis must be closed in the correct order. Therefore, )( and ()(() are invalid.'''

#Solution : Time Complexity : O(n) where n is the length of the expression
#Space Complexity : O(n) 
def is_balanced(exp):
    closing = ['}', ')', ']']
    stack = My_Stack()
    
    for character in exp:
        if character in closing:
            # If the stack is empty, there's no opening bracket
            # to match with, so the expression is unbalanced
            if stack.is_empty():
                return False
            
            #pop the top element from the stack (most recent opening bracket)
            top_element = stack.pop()
            
            if character == '}' and top_element != '{':
                return False
            if character == ')' and top_element != '(':
                return False
            if character == ']' and top_element != '[':
                return False
        else:
            # If the character is not a closing bracket,
            # push it onto the stack
            stack.push(character)
    
    # If stack is not empty, stack contains unmatched opening parentheses
    if not stack.is_empty():
        return False
    
    return True

#Challenge : Min Stack-----------------------
'''
Design a stack data structure to retrieve the minimum value in O(1) time. The following functions must be implemented:
    min(): Returns the minimum value in the stack in constant time.
    push(int value): Pushes a value onto the stack.
    pop(): Removes and returns a value from the top of the stack.
All functions should be implemented with a time complexity of O(1).'''

#Solution : Time Complexity : All of the operations have a time complexity of O(1)
#Space Complexity : Push Operation has a space complexity of O(n) as we use two stacks to store the values, while pop and min operations have a space complexity of O(1). 
class Min_Stack:
    def __init__(self):
        self.main_stack = My_Stack()
        self.min_stack = My_Stack()
        
    def pop(self):
        # Removes and returns the top value from the stack
        self.min_stack().pop()
        return self.main_stack().pop()
    
    def push(self, value):
        # Pushes a value onto the stack
        self.main_stack.push(value)
        if self.min_stack.is_empty() or self.min_stack.peek() > value:
            self.min_stack.push(value) # Push new value onto the min_stack
        else:
            self.min_stack.push(self.min_stack.peek()) # Again, push the top value onto min_stack
    
    def min(self):
        #return min value from stack
        return self.min_stack.peek()

