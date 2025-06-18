my_iter = iter([1,2,3,4])
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

#Iterators can be implemented as classes; you just need to implement the __next__ and __iter__ methods. Here’s an example of a class that mimics the range function, returning all values from a to b:

class My_Range:
    def __init__(self, a= 0, b=0):
        self.a = a
        self.b = b
    
    def __iter__(self):  # returns the iterator object itself
        return self
    
    def __next__(self) : # returns the next item in the sequence
        if self.a < self.b:
            value = self.a 
            self.a += 1
            return value
        else:
            raise StopIteration  # raises StopIteration when there are no more items to return
        
my_range = My_Range(1,5)
# print(my_range.next())
# print(my_range.next())
# print(my_range.next())
# print(my_range.next())

# for value in My_Range(1, 8):
#     print(value)

# Printing even number
class Even_Number_Iterator:
    def __init__(self, n):
        self.n = n
        
    def __iter__(self):
        return self
    
    def __next__(self):
        even_array = []
        for i in range(1, self.n + 1):
            if i % 2 == 0:
                even_array.append(i)
        return even_array

my_range = Even_Number_Iterator(10)
print(my_range.__next__())

#Fibonacci series
class Fibonacci_Iterator:
    def __init__(self, n):
        self.n = n
        
    def __iter__(self):
        return self
    
    def __next__(self):
        fibo_array = []
        a = 0
        b = 1
        fibo_array.append(a)
        
        for _ in range(self.n):
            next = a + b
            a = b
            b = next
            fibo_array.append(a)
        return fibo_array

my_range = Fibonacci_Iterator(10)
print(my_range.__next__())