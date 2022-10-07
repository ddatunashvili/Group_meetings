

var = """
def func(a,b):
    return a + b
"""

exec(var)

print(func(1,2))



var = "print(1+2)"

eval(var)






# Simple multiplication

def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    return number * 9


# Find Maximum and Minimum Values of a List
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)


# string formating
def greet(name):
    return f"Hello, {name} how are you doing today?"



