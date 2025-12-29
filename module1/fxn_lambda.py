# Built-in and user-defined functions

# example of a built-in function
numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # len() -> return length of list i.e Output: 5
# enumerate() -> return index and value as tuple i.e Output: [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(enumerate(numbers)))
print(float(numbers[3]))  # float() -> convert integer to float i.e Output: 4.0
# type() -> return type of variable i.e Output: <class 'list'>
print(type(numbers))
# sorted() -> return sorted list in descending order i.e Output: [5, 4, 3, 2, 1]
print(sorted(numbers, reverse=True))

# user-defined function


def greet(name="Bob"):
    return f"Hello, {name}!"


greeting = greet("Alice")  # Output: Hello, Alice!
# replaces default parameter with provided argument
greeting2 = greet()  # Output: Hello, Bob!
print(greeting)
print(greeting2)


def add(a, b):
    print(f"Adding {a} and {b} gives {a + b}")


add(3, 5)  # Output: Adding 3 and 5 gives 8
add(b=1, a=2)  # keyword arguments, Output: 3 NOTE: arguments can be in any order

# If you do not know how many arguments will be passed into your function, add a * before the parameter name.
# If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.


def my_function(title, *args, **kwargs):
    print("Title:", title)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


my_function("User Info", "Emil", "Tobias", age=25, city="Oslo")

# a variable created inside a function is local to that function


def my_func():
    x = 10
    print("Value inside function:", x)


my_func()
# print(x) # This would raise an error

# can use global variable to be used inside or outside function

# lambda function
# A lambda function can take any number of arguments, but can only have one expression.


def square(x): return x ** 2


print(square(5))  # Output: 25

# Recursion


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))  # Output: 120
