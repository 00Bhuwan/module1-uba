# variable_name = value 

'''Some examples to create variables'''
word = 'Welcome'
num = 12
pi = 3.14
is_valid = True
list_fruits = ['apple', 'banana', 'cherry']
dict_person = {'name': 'Alice', 'age': 30}
tuple_num = (1, 2.99)

# we can create multiple variables in one line
a, b, c = 1, 2, 3 
x, y, z = [10, 20, 30]  # also called data unpacking
print(a, b, c)
print(x, y, z)

# also class can be stored in variables
class Dog: pass
my_dog = Dog()
# my_dog is now an instance of Dog class

print("Printing variable types")
print(type(word))              # 'str' type
print(type(num))        # 'int' type    
print(type(pi))      # 'float' type
print(type(is_valid))   # 'bool' type
print(type(list_fruits))    # 'list' type
print(type(dict_person))    # 'dict' type
print(type(tuple_num))    # 'tuple' type
print(type(my_dog))     # '__main__.Dog' type where Dog is class name


# Data types

# 1. Numeric Data Types
# int stands for integer 
int_var = 12
# represents whole number without decimal point

# float 
float_var = 3.14
# represents floating point number with decimal point

# complex 
complex_var = 1 + 2j
# represents complex number with real and imaginary parts

# 2. Sequence Data Types
# str stands for string
str_var = ''
# any text inside single or double quotes is string
str_var1 = "Hello, World!"
str_var2 = 'Python Programming'

# list
list_var = [1, 2, 3, 'apple', 'banana']
# lists are mutable (can be changed after creation)
list_var[3] = 'orange' # change apple to orange using index value

# tuple
tuple_var = (1, 2, 3, 'apple', 'banana')
# tuples are immutable (cannot be changed after creation)

# 3. Mapping Data Type: Dictionary
dict_var = {'name': 'Alice', 'age': 30}
# key-value pairs, unordered, mutable

# 4. Set Data Types
# set
set_var = {1, 2, 3, 'apple', 'banana'}
# unordered collection of unique items, mutable
# i.e cannot acces using index value set_var[0] will raise error
set_eg = {1,2,'ram', [1,5], True}

# frozenset
frozenset_var = frozenset([1, 2, 3, 'apple'])
# immutable version of set

# 5. Boolean Data Type
bool_var = True  # or False

# None Type
none_var = None
# represents absence of value or null value

# Type Casting / Type Conversion
# Python atomatically converts data types as needed without expliciltly mentioning it
#example
num = 12     # int: nowhere mentioned integer during declaration
pi = 3.14    # float: nowhere mentioned float during declaration
result = 10 + 3.5  # int 10 is automatically converted to float 10.0

# but we can also manually convert using built-in functions
# int(), float(), str(), list(), tuple(), dict(), set()

print("\nType Casting Examples")
word = 'Welcome'
num = 12
pi = 3.14
is_valid = True
list_fruits = ['apple', 'banana', 'cherry']
dict_person = {'name': 'Alice', 'age': 30}
tuple_num = (1, 2.99)

# examples 
# int(word)                             # will raise ValueError
print(float(num))                       # converts integer to float
print(int(pi))                          # converts float to integer (removes decimal part)
print(str(is_valid))                    # converts boolean to string
print(list(tuple_num))                  # converts tuple to list
print(tuple(list_fruits))               # converts list to tuple
print(dict([('name', 'Alice'), ('age', 30)])) # creates dictionary from list of tuples
print(set(list_fruits))                 # converts list to set
# set conversion removes duplicates if any