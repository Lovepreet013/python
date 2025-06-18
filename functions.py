import math

def repeat(s : str, exclaim : bool) -> str : #these are type hints
    result = s + s #or result = s * 2 which is faster
    if exclaim : 
        result = result + '!!'
    return result

def main() :
    print(repeat("Yay", True))
    print(repeat("Haha", False))

if __name__ == "__main__" : #this only when we are running this file directly in terminal. In this __name__ = __main__
    main() 

def MathOp():
    classic_divison = 3/2
    floor_division = 3//2
    modulus = 3%2
    power = 3**2

    return [classic_divison, floor_division, modulus, power]

[classic_division, floor_division, modulus, power] = MathOp()
print(f"Classic Division: {classic_division}, Floor Division: {floor_division}, Modulus: {modulus}, Power: {power}")


def check_parity(num : int) -> int :
    result = (num % 2)
    return result

def in_range(x : int, y : int) -> bool:
    return (x < 1/3 < y)

def find_occurance(s : str, ch : str) -> int:
    count = 0
    for i in s:
        if i == ch:
            count += 1
    return count

occurance = find_occurance("hello world", "l")
print(f"Number of occurances of 'l' in 'hello world': {occurance}")

def remove_List():
    l1 = [1,2,3,4,5,6,7]
    l2 = [2,3,4]
    l1.remove(l2[0])
    l1.remove(l2[1])
    l1.remove(l2[2])

    return l1

l = remove_List()
print(l)

def greatest_common_divisor(a : int, b : int) -> int :
    return math.gcd(a, b)
print(greatest_common_divisor(24, 18))

def gcd(a, b) :
    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd
print(gcd(8, 12))

#Recursion-----
def factorial(n) :
    if(n == 0 or n == 1):
        return 1
    else : 
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120

def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))
    
number = int(input("Enter a number for Fibonacci series: "))
for i in range(number):
    print(fibonacci(i), end=' ')

def sum_natural_numbers(n):
    if n <= 1:
        return 1
    else :  
        return n + sum_natural_numbers(n - 1)

num = sum_natural_numbers(5)
print(num)  # Output: 15

#loop
def find_max_value(lst):
    if not lst:
        return None
    max_value = lst[0]
    index = 0

    for i, value in enumerate(lst):
        if value > max_value:
            max_value = value
            index = i

    return [max_value, index]

list = [23,66,11,2,98,100,22,1,3,4]
result = find_max_value(list)
print(result)

def reverse_list(lst):
    s = len(lst)

    new_list = [None] * s

    for i in lst:
        s = s - 1
        new_list[s]= i
    return new_list

print(reverse_list([1, 2, 3, 4, 5]))

def has_duplicates(lst):
    flag = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                flag = 1
                break
    if flag == 1:
        return True
    else:
        return False

print(has_duplicates([1,2,3,4,6,7,8,9,10]))

def print_even_odd(n):
    i = n
    for _ in range(n):
        if(i >= 0):
            if(i % 2 == 0):
                print(f"{i} is even")
                i -= 1
            else :
                print(f"{i} is odd")
                i -= 1

print_even_odd(11)