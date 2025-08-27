def foo():
    return "I am foo"

list1 = [1,2,3,4, "Hello",True,foo] #ordered sequence of heterogeneous elements

list1.append(5) #O(1) operation
list1.insert(0, 0) #O(n) operation
list1.remove(3) #O(n) operation
list1.pop() #O(1) if index is not specified it removes the last element else #O(k) operation where k < n
list1.reverse() #O(n) operation

#List slicing
list1[1:4] #returns a new list with elements from index 1 to 3
list1[1:4:1] #returns a new list with elements from index 1 to 3 with step 1
list1[1:4] = [10, 20, 30] #replaces elements from index 1 to 3 with new elements
del list1[1:4] #deletes all the elements from index 1 to 3
print(list1)

def remove_even_numbers(lst): #time complexity O(n), Space complexity O(1)
    return [x for x in lst if x % 2 != 0] #list comprehension to filter out even numbers