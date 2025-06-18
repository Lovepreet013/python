def my_range(a, b):
    while a < b :
        yield a 
        a += 1

a = my_range(1, 10)
# print(next(a))  
# print(next(a))  

# for value in my_range(1, 10):
#     print(value)

def square(n)  :
    for value in range(n):
        yield value * value

b = square(10)
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b)) here we get error as we pass 10 in square function

def odd(n):
    for i in range(n):
        if i % 2 != 0:
            yield i
            
c = odd(10)
# print(c) this will print the generator object address

for value in c:
    print(value)
    

def reverse_from_number_to_zero(n):
    for value in range(n, -1, -1):
        yield value

for i in reverse_from_number_to_zero(10):
    print(i)

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("fibonacci sequence up to 10 terms:")
for value in fibonacci(10):
    print(value)