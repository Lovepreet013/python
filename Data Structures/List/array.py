'''In Python, an array is just an ordered sequence of homogeneous elements. In other words, an array can only hold elements of one datatype. Python arrays are basically just wrappers for C arrays. The type is constrained and specified at the time of creation. Arrays are more storage efficient as compared to lists.
List have a block of pointers to the objects, while arrays have a block of contiguous memory locations for the objects. This makes arrays more memory efficient than lists. However, arrays are less flexible than lists as they can only hold elements of one datatype.'''

import array
new_array = array.array('f', [1.0, 2.0, 3.0, 4.0])  # 'f' is the type code for float

another_array = array.array('i', [1, 2, 3, 4])  # 'i' is the type code for signed integer

another_array.append(5)  # O(1) operation

# extend() appends iterable to the end of the array
another_array.extend([6, 7])  # O(k) operation where k is the number of elements to be added

del another_array[2]

print(another_array[1:3])  # 2nd to 5th
print(another_array[:-3])  # beginning to 3rd
print(another_array[3:])  # 6th to end
print(another_array[:])   # beginning to end