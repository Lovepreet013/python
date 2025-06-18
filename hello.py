# This is comment in Python language
import numpy as np

msg = "Hello World!!"
# print(msg)

print(np.random.randint(1,9))

s = "This is example string!!"

s.lower().upper()
print(s.startswith(" This"), s.endswith("!! "))
s.find("example")
s.replace("old", "new")
s.split(" ") # s.strip() removes leading and trailing whitespace and returns list
print(s.strip())
print(s[0:6]) # 6th character is not included

print(s[::-1])


value = 2.7899999
print(f"{value: .2f}") # f-string formatting, .2f means 2 decimal places

car = {'tires' : 4, 'color' : 'red', 'door' : 2}
print(f'car={car}')


address_book = [
    {'name':'N.X.', 'addr':'15 Jones St', 'bonus': 70},
    {'name':'J.P.', 'addr':'1005 5th St', 'bonus': 400},
    {'name':'A.A.', 'addr':'200001 Bdwy', 'bonus': 5},
]

for person in address_book:
    print(f'{person["name"]:10} || {person["addr"]:20} || {person["bonus"]:10}')


#in
squares = [1, 4, 9, 16, 25]
sum = 0
for num in squares:
    sum+= num
print(sum)

lst = ['larry', 'curly', 'lavi']
if 'lavi' in lst:
    print("Lavi is in the list")


the_string = "Hello World"
for ch in the_string:
    print(ch)

#list methods
lst = [1, 2, 3, 4, 5]
lst2 = [7, 8, 9]
lst.append(6)  # add 6 at the end. Does not return the new list, just modifies the original.
lst.insert(2, 10)  # insert 10 at index 2, shifting elements to the right
lst.extend(lst2) # adds the elements in list2 to the end of the list
lst.index(2)  # returns the index of the first occurrence of 2
lst.remove(2) # removes the first occurrence of 2
lst.sort()  # sorts the list in ascending order, does not return the new list
lst.reverse()  # reverses the list in place, does not return the new list
lst.pop() #removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append())


#sorted()
lst = ["aaa", "bb", "cccc"]
sorted(lst) # returns a new sorted list, does not modify the original list
sorted(lst, reverse=True)  # returns a new sorted list in descending order
sorted(lst, key=len) # sorts the list based on the length of the elements (if they are strings)
# sorted(lst, key=str.lower)   sorts the list based on the lowercase version of the elements (if they are strings)

## Say we have a list of strings we want to sort by the last letter of the string.
strs = ['xc', 'zb', 'yd' ,'wa']

## Write a little function that takes a string, and returns its last letter.
## This will be the key function (takes in 1 value, returns 1 value).
def MyFn(s):
    return s[-1]

## Now pass key=MyFn to sorted() to sort by the last letter:
print(sorted(strs, key=MyFn))  ## ['wa', 'zb', 'xc', 'yd']

#Tuples
tuple = (1, 2, 'hi')
print(len(tuple))  ## 3
print(tuple[2])    ## hi
# tuple[2] = 'bye'  ## NO, tuples cannot be changed
tuple = (1, 2, 'bye')  ## this works
tuple = ('hi',)   ## size-1 tuple, comma is required

#List Comprehensions
nums = [1, 2, 3, 4]
squares = [ n * n for n in nums ]   ## [1, 4, 9, 16]


strs = ['hello', 'and', 'goodbye']
shouting = [ s.upper() + '!!!' for s in strs ]
## ['HELLO!!!', 'AND!!!', 'GOODBYE!!!']

#Dictionary: key/value hash table structure
dict = {}
dict['a'] = 1
dict['b'] = 2
dict['c'] = 3

print(dict.get("a"))
dict.keys() #returns new list of keys
dict.values() #returns new list of value

#dict formatting
h = {}
h['word'] = 'garfield'
h['count'] = 42
# s = 'I want %(count)d copies of %(word)s' % h  # %d for int, %s for string
# 'I want 42 copies of garfield'

# You can also use str.format().
# s = 'I want {count:d} copies of {word}'.format(h)

#dict del operator
var = 6
del var  # var no more!

list = ['a', 'b', 'c', 'd']
del list[0]     ## Delete first element
del list[-2:]   ## Delete last two elements
print(list)      ## ['b']

dict = {'a':1, 'b':2, 'c':3}
del dict['b']   ## Delete 'b' entry
print(dict)      ## {'a':1, 'c':3}

file = open('hello.txt', 'a+', encoding='utf-8')  # open file for writing

file.write('This is written to file using write() method.\n')
file.seek(0) # move the cursor to the beginning of the file

for line in file:
    print(line, end='')
file.close()

# for i in range(5):
#     print(i)

i = 0

while (i < 5):
    print(i)
    i += 1


# age = input("Enter your age : ")
# print(f"You entered: {age}")

#List comprehension 
print([x * x for x in [1,2,3,4,5,6]])
print([x * x for x in range(10) if x % 2 == 0])


my_list = ["a","b","c","d"]
for i, value in enumerate(my_list):
    print(f'Index : {i} Value : {value}')

for x in "Full Speed Python":
  print(x)

