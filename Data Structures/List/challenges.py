#Challenge: Merge Two Sorted Lists----------------

#Solution 1 : Using a new list and three pointers
def merge_sorted_lists(lst1, lst2): # time complexity O(m+n) where m is len of lst1 and n of lst2, Space complexity O(m+n) for the new list
    
    result = [None] * (len(lst1) + len(lst2))  # Preallocate space for the merged list
    
    p1, p2, p3 = 0, 0, 0  # Pointers for lst1, lst2, and result
    
    while(p1 < len(lst1) and p2 < len(lst2)):
        # If the value at p1 is smaller than value at p2, store the value at p3 and increment p1 and p3
        if(lst1[p1] < lst2[p2]):
            result[p3] = lst1[p1]
            p1 += 1
            p3 += 1
        # Otherwise, store the value at p2 into p3 and increment p2 and p3
        else : 
            result[p3] = lst2[p2]
            p2 += 1
            p3 += 1
    # Case : if elements remain in lst1, store them in result
    while(p1 < len(lst1)):
        result[p3] = lst1[p1]
        p1 += 1
        p3 += 1
    
    # Case : if elements remain in lst2, store them in result
    while(p2 < len(lst2)):
        result[p3] = lst2[p2]
        p2 += 1
        p3 += 1
    
    return result

#Solution 2 : Merging in place i.e no new list is created
# Considering the impact of insert(), time complexity is O((m+n) * m) in worst case where m is len of lst1 and n of lst2. This is because for each insertion from lst2 into lst1, up to m elements might need to be shifted.
# Space complexity O(m+n) as no new list is created
def merge_sorted_lists_in_place(lst1, lst2):
    p1, p2 = 0, 0 
    
    while p1 < len(lst1) and p2 < len(lst2):
        if lst1[p1] > lst2[p2]:
            lst1.insert(p1, lst2[p2])
            p1 += 1
            p2 += 1
        else : 
            p1 += 1
            
    # If there are remaining elements in lst2, append them to lst1
    if p2 < len(lst2):
        lst1.extend(lst2[p2 : ]) #here if we use append() it will add the entire list as a single element, so we use extend() to add elements individually
    
    return lst1

l1 = [23, 33, 35, 41, 44, 47, 56, 91, 105]
l2 = [32, 49, 50, 51, 61, 99, 110]

result = merge_sorted_lists(l1, l2)
# print(result)

#Challenge: Find Two Numbers That Add Up to K------------------

#Solution 1 : Using a naive approach, comparing each element directly with other 
# Time Complexity : O(n^2) where n is the length of the list , Space Complexity : O(1)
def find_two_numbers(lst, k):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == k:
                result.append(lst[i])
                result.append(lst[j])
                return result

#Solution 2 : We use TWO POINTERS
'''
Below are the detailed steps of the algorithm:
Sort the input list in non-decreasing order.
Initialize two pointers, the left pointing to the beginning of the list and the right pointing to the end of the list.
While left is less than right:
    Calculate the sum of elements at left and right.
    If the sum is less than k, increment the left pointer.
    If the sum is greater than k, decrement the right pointer.
    If the sum is equal to k, append the elements at left and right to the result list and exit the loop.
Return the result list containing elements that sum up to k.'''

#Time complexity is O(n log n), where n i number of elements in the list. The Sorting of the list takes O(n log n) time, and loop iterates through the sorted list only once, which takes O(n) in the worst case scenario.
#Space complexity is O(1).

def find_two_number_two_pointers(lst, k):
    lst.sort()  # Sort the list in non-decreasing order
    
    result = []
    
    left = 0
    right = len(lst) - 1
    
    #Iterate until the pointers meet
    while left < right:
        #calcutate the sum of elements at left and right
        sum = lst[left] + lst[right]
        
        #if the sum is less than k, increment the left pointer
        if sum < k:
            left += 1
        
        #if the sum is greater than k, decrement the right pointer
        elif sum > k:
            right -= 1
        
        #if the sum is equal to k, append the elements at left and right to the result list and exit the loop
        else:
            result.append(lst[left])
            result.append(lst[right])
            break
    
    return result


#Solution 3 : Using Binary Search
'''
First, the list is sorted to arrange the elements in ascending order, enabling efficient searching. Then, for each element in the sorted list, we compute the difference between the target sum (k) and the current element (ai). This difference represents the value we need to find in the list to achieve the target sum. By utilizing binary search, we attempt to locate this difference within the sorted list. This process is repeated for each element in the list until a pair that sums up to the target is found.
'''
# Time complexity : The time complexity of this solution is O(nlog⁡n). The sorting of the list takes O(nlogn), and binary search takes O(logn) time to find single element. 
# Space Complexity : O(1)
def binary_search(a, item):
    first = 0
    last = len(a) - 1
    
    found = False
    index = -1
    
    # Perform binary search until the item is found or the pointers meet
    while first <= last and not found:
        midpoint = (first + last) // 2
        
        # Check if the middle element is the item
        if a[midpoint] == item:
            #If found, update the index and set found to True
            index = midpoint
            found = True
        else:
            # If the item is smaller than the middle element, update the last pointer
            if item < a[midpoint]:
                last = midpoint - 1
            
            # If the item is larger than the middle element, update the first pointer
            else :
                first = midpoint + 1    
    
    if found:
        return index
    else:
        return -1

def find_sum(lst, k):
    lst.sort()  # Sort the list in non-decreasing order
    
    for i in range(len(lst)):
        # Find the index of the complement to the current element using binary search
        index = binary_search(lst, k - lst[i])
        
        #If the complement is found and it's not the same element, return the pair
        if index != -1 and index != i:
            return [lst[i], k - lst[i]]
    
    return []

# print(find_sum([1, 4, 3, 5, 5], 10))


#Challenge : Product of Array Except Self--------------
#Statement : You’re given an integer array, nums. Return a resultant array product so that product[i] is equal to the product of all the elements of nums except nums[i]. Write an algorithm that runs in O(n) time without using the division operation.

#Solution 1 : Brute Force
'''In this approach, we maintain a variable 'left' , which represents the cumulative product of all elements to the left of the current element being considered. This 'left' variable is crucial because it also helps us compute the product of all elements to the right of the current index.

By multiplying the product of subsequent elements with the cumulative product of elements to the left, we ensure that every element’s product is accurately calculated and updated in the result list. This iterative process covers all elements in the list, ensuring that the product of every element in the original list, excluding the current element itself, is correctly computed.'''

#Time complexity :  O(n^2), Space Complexity : O(1)
def find_product(lst): 
    product = []
    left = 1
    
    for i in range(len(lst)):
        current_product = 1
        
        #Compute the product of values to the right of the current index
        for values in lst[i + 1 :]:
            current_product *= values
        
        #Append the product of current element and product of all the left elements to product
        product.append(current_product * left)
        
        #Update 'left' by multiplying with the current element
        left *= lst[i]
    
    return product

# print(find_product([10, 12, 19, 111, 15]))

#Solution 2 : Bidirectional product accumulation
'''The algorithm first starts by traversing the list from left to right, accumulating the product of all encountered numbers up to the current index while keeping track of the left product. It then iterates through the list from right to left, computing the product of all elements to the right of the current index. At each index, this product is multiplied by the accumulated left product till that index to obtain the final result. After completing both passes, the list will contain the desired product list output.

Here’s the algorithm:
Left product calculation:
    We start with left = 1 and iterate through the list from left to right.
    At each step, we accumulate the product of all encountered numbers up to the current index.
    We store this cumulative product in a product list.
    Simultaneously, we update left by multiplying it with the current element in the list.

Right product calculation:
    Similarly, we start with right = 1 and iterate through the list from right to left.
    We update the elements in the product list by multiplying them with right, which represents the product of all elements to the right of the current index.
    Simultaneously, right is updated by multiplying it with the current element in the list.
'''

#Time Complexity : O(n). The algorithm performs two passes through the list, each taking O(n) time.
#Space Complexity : O(1)

def find_product_(lst):
    product = []
    
    left = 1
    right = 1
    
    #First pass : Calculate products starting from left
    for values in lst:
        product.append(left)
        left *= values
    
    #Second pass : Update the product list by calculating products from right to left
    for i in range(len(lst)-1, -1, -1 ):
        product[i] = product[i] * right
        right = right * lst[i]
    
    return product
    
# print(find_product_([10, 12, 19, 111, 15]))


#Challenge : Find the minimum in the list------------
#Solution : We can use sort() and return 1st element. This will have Time complexity of O(nlogn) because of sort() and Space complexity of O(1)

#Solution 2 : We can use min() function which will have Time complexity of O(n) and Space complexity of O(1)

#Solution 3: Linear search, Time Complexity O(n) and Space Complexity O(1)
def find_min(lst):
    min = lst[0]  # Initialize min with the first element of the list
    
    for i in range(1, len(lst)):
        if lst[i] < min:
            min = lst[i]
    
    return min

#Challenge : First Non-Repeating Integer in a List---------------

#Solution : Brute force using two pointers. Time Complexity O(n^2) and Space Complexity O(1)
def find_first_unique(lst):
    # Iterate through each element in the list
    for p1 in range(len(lst)):
        p2 = 0
        
        #Compare the current element (p1) with all other elements (p2)
        while(p2 < len(lst)):
            if(p1 != p2 and lst[p1] == lst[p2]):
                break
            p2 += 1
        
        # If p2 reaches the end of the list, the element at p1 is unique
        if(p2 == len(lst)):
            return lst[p1]
    
    return None

# print(find_first_unique([2,3,4,4,6,7,2,3,8]))

#Challenge: Find Second Maximum Value in a List------------------

#Solution : Traverse the list
#Time Complexity O(n) and Space Complexity is O(1)
def find_second_max_value(lst):
    max = float('-inf')
    second_max = float('-inf')
    
    for i in lst:
        if i > max:
            second_max = max
            max = i
        
        # If the current number is greater than the second maximum and not equal to first_max
        elif i != max and i > second_max:
            second_max = i
            
    return second_max if second_max != float('-inf') else None

# print(find_second_max_value([3,5,1,3,8,9,12,10,11,15,51]))

#Challenge: Rotate List-----------------------
'''
Statement:
Given a list, nums, and an integer, k, rotate the list to the right by k positions so that each rotation involves shifting the elements one position at a time.'''

#Solution 1 : 
'''The brute force approach involves iterating through the list once. For each element in the list, we determine its new position after rotation by adding the number of positions we want to rotate the list to the index of each element. To handle cases where the new index exceeds the length of the list, we take the modulo of the list length. This ensures that the element wraps around to the beginning of the list if necessary. Once we’ve determined the new index, we place the element at that position in the rotated list. This process is repeated for every element in the original list, ensuring all elements are correctly positioned after rotation.'''

#Time complexity : O(n), Space Complexity : O(n) as we create a new list for rotated elements
def right_rotate(lst, k):   
    #if the length of list is 0 or k is 0, no rotation is needed
    if(len(lst) == 0 or k == 0):
        return lst
    else : 
        #For k greater than length of list, we can just take k modulo length of list
        k = k % len(lst)
    
    rotated_list = []
    
    # Get the elements from the end and append them to rotatedList
    for item in range(len(lst) - k, len(lst)):
        rotated_list.append(lst[item])
    
    # Get the remaining elements and append them to rotatedList
    for item in range(0, len(lst) - k):
        rotated_list.append(lst[item])
    
    return rotated_list

#Solution 2 : Slice and Shift rotation
#Time Complexity : O(n), Space Complexity : O(n) as we create a new list for rotated elements
def rotate_right(lst, k):
     #if the length of list is 0 or k is 0, no rotation is needed
    if(len(lst) == 0 or k == 0):
        return lst
    else : 
        #For k greater than length of list, we can just take k modulo length of list
        k = k % len(lst)
    
    #perform rotation by slicing the list
    rotated_list = lst[-k : ] + lst[ : -k]
    
    return rotated_list

# print(rotate_right([1, 2, 3, 4, 5, 6, 7], 2))


#Challenge : Rearrange Positive & Negative Values--------------------

#Solution 1 : Using Auxiliary lists
#Time Complexity : O(n), Space Complexity : O(n) as we create two new lists for negative and positive values
def rearrange_positive_negative(lst):
    neg = []
    pos = []
    
    #Make a list of negative and positive values
    for i in lst:
        if i < 0:
            neg.append(i)
        else :
            pos.append(i)
    
    return neg + pos

#Solution 2 : In-place rearrangement
'''In this solution, we will not use additional space to reach the desired output. The steps of the algorithm are as follows:

    Initialize leftMostPosEle to 0, representing the index of the leftmost positive element. This variable tracks where the next positive number should be placed.
    Iterate through the list using a for loop from index 0 to the end of the list.
    At each iteration, check if the current element is negative (lst[curr] < 0).
    If the current element is negative and it’s not the most recent negative number encountered (i.e., if curr is not equal to leftMostPosEle), then swap the current element with the leftmost positive element. This move effectively places the current negative number to the left of all positive numbers encountered so far.
    After each swap, increment leftMostPosEle by 1 to ensure it always points to the correct position for the next positive number.
    Once all iterations are complete, return the rearranged list.
'''
#Time Complexity : O(n), Space Complexity : O(1) as we do not use any additional space except for a few variables
def rearrange(lst):
    #When we find a negative number at some position i, we want to move it left, as far as possible — before all positive numbers we've already seen. That’s where left_most_positive_number helps.
    
    left_most_positive_number = 0
    
    for i in range(len(lst)):
        #if negative number
        if lst[i] < 0:
            #if it is not the last negative number
            if i != left_most_positive_number:
                #Swap the two
                lst[i], lst[left_most_positive_number] = lst[left_most_positive_number], lst[i]
            #Update the last position
            
            left_most_positive_number += 1
    
    return lst


#Solution 3 : pythonic way
#Time Complexity : O(n), Space Complexity : O(m+n), m = neg elements, n = pos elements
def rearrange_(lst):
    return [x for x in lst if x < 0] + [x for x in lst if x >= 0]

# print(rearrange_([1, -2, 3, -4, 5, -6, 7, -8, 9, 10]))

#Challenge : Rearrange Sorted List in Max/Min Form

# Solution 1 : Create a new list
#Time Complexity : O(n), Space Complexity : O(n) as we create a new list
def rearrage_list_max_min(lst):
    if(len(lst) == 0):
        return []
    
    result = []
    mid = len(lst) // 2
    
    # Iterate through half of the sorted list
    for i in range(mid):
        # Append the largest remaining element (from the end of the list)
        result.append(lst[-(i + 1)])
        
        # Append the smallest remaining element (from the start of the list)
        result.append(lst[i])
    
    if len(lst) % 2 == 1:
        result.append(lst[mid])
        
    return result

# print(rearrage_list_max_min([1, 2, 3, 4, 5, 6, 7, 8]))

def max_min_arrangement(lst):
    p1 = 0
    p2 = len(lst) - 1
    result = []

    while p1 < p2:
        result.append(lst[p2])  # max
        result.append(lst[p1])  # min
        p1 += 1
        p2 -= 1

    if p1 == p2:
        result.append(lst[p1])  # middle element for odd-length list

    return result

#Solution 3 : Use modulus (%) and two pointers, Works only for integers (not floats or strings)
#Time complexity : O(n), Space Complexity : O(1)
def rearrange_list(lst):
    if(len(lst) == 0):
        return []
    
    #Initailize two pointer to the start and end of the list
    max_idx = len(lst) - 1
    min_idx = 0
    
    # Initialize a variable larger than any element in the list to use for encoding
    max_elem = lst[len(lst) - 1] + 1
    
    #Encoding Phase
    for i in range(len(lst)):
        if i % 2 == 0: #Encoding at even indexes
            lst[i] = lst[i] + (lst[max_idx] % max_elem) * max_elem
            max_idx -= 1
        
        else: #Encoding for odd indexes
            lst[i] = lst[i] + (lst[min_idx] % max_elem) * max_elem
            min_idx += 1
            
    #Decoding phase
    for i in range(len(lst)):
        lst[i] = lst[i] // max_elem
    
    return lst

# print(rearrange_list([1, 2, 3, 4, 5, 6, 7, 8]))

#Challenge : Maximum Sublist ----------------------
'''Statement
Given an unsorted list nums, find the sum of the maximum sum sublist. The maximum sum sublist is a list of contiguous elements in nums for which the sum of the elements is maximum.'''

'''The steps of the algorithm are given below:

    Initialize a curr_max variable to keep track of the maximum sum of the current list index and another global_max variable to keep track of the largest sum seen so far. Both variables will be initialized with the first element of nums.

    Traverse the list from the second element until the end of the list is reached.

    While traversing, if curr_max is less than 0, assign it the element at the current index. Otherwise, add the element at the current index to curr_max.

    Next, if global_max is less than curr_max, reassign it to curr_max.'''

#Time Complexity : O(n), Space Complexity : O(1)
def find_max_sum_sublist(lst):
    if len(lst) < 1:
        return 0
    
    curr_max = lst[0]
    global_max = lst[0]
    
    for i in range(1, len(lst)):
        if curr_max < 0:
            curr_max = lst[i]
        else:
            curr_max += lst[i]
        
        if global_max < curr_max:
            global_max = curr_max
    
    return global_max

print(find_max_sum_sublist([4,-1,2,-7,3,4]))