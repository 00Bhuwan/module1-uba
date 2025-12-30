# symbols or keywords to perform operations on operands :-> operator

# Built-in Operators in Python are

# 1. Arithmetic Operators
x, y = 2, 3
addition = x + y          # Addition : 5
subtraction = x - y       # Subtraction : -1
multiplication = x * y    # Multiplication : 6
division = x / y         # Division : 0.666
modulus = x % y          # Modulus : 2 (gives remainder)
exponentiation = x ** y   # Exponentiation : 8 (2^3)
floor_division = y // x   # Floor Division : 1 (gives integer part of division)

# 2. Comparison Operators
a, b = 5, 10
equal = (a == b)          # Equal : False
not_equal = (a != b)      # Not Equal : True
greater_than = (a > b)    # Greater Than : False
less_than = (a < b)       # Less Than : True
greater_equal = (a >= b)  # Greater Than or Equal To : False
less_equal = (a <= b)     # Less Than or Equal To : True

# 3. Logical Operators
p, q = True, False
logical_and = p and q     # Logical AND : False
logical_or = p or q      # Logical OR : True
logical_not = not p       # Logical NOT : False
# Note: Python does not have a specific operator for 'nor', 'nand', 'xnor'.
nor_eg = ~(6|3)  # : -8  Example of NOR using bitwise NOT and OR 
nand_eg = ~(6&3) # : -2  Example of NAND using bitwise NOT and AND
xnor_eg = ~(6^3) # : -6  Example of XNOR using bitwise NOT and XOR

# 4. Assignment Operators
m = 10
m += 5                    # m = m + 5 : 15
m -= 3                    # m = m - 3 : 7
m *= 2                    # m = m * 2 : 20
m /= 4                    # m = m / 4 : 2.5  (/= always results in float)
m //= 4                   # m = m // 4 : 2   (//= results in integer if both operands are integers)
m %= 4                    # m = m % 4 : 2.0
m **= 3                   # m = m ** 3 : 1000

# 5. Bitwise Operators
a, b = 6, 3  # In binary: 6 = 110, 3 = 011
bitwise_and = a & b       # Bitwise AND : 2 (010 i.e 1&1=1)
bitwise_or = a | b        # Bitwise OR : 7 (111 i.e 0|0=0)
bitwise_xor = a ^ b       # Bitwise XOR : 5 (101 i.e 0 for same, 1 for different)
bitwise_not_a = ~a        # Bitwise NOT : -7(inverts bits) 6=110 -> ~6=001+1=7 (invert i.e -7)
left_shift = a << 1       # Left Shift : 12 (0110 left shift by 1 is 1100)
right_shift = a >> 1      # Right Shift : 3 (011)


# 6. Membership Operators
fruits = ['apple', 'banana', 'cherry']
is_apple_in_fruits = 'apple' in fruits        # Membership IN : True
is_grape_not_in_fruits = 'grape' not in fruits  # Membership NOT IN : True

# 7. Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]        #or use c = a.copy()

print(a is b)          # Output: True (a and b refer to the same object)
print(a is c)         # Output: False (a and c refer to different objects with same content)
print(a is not c)      # Output: True (a and c refer to different objects)

# some operators behave differently based on data types
# e.g for strings
str1 = "Hello"
str2 = "World"

concat = str1 + " " + str2  # Concatenation : "Hello World"
repeat = str1 * 3           # Repetition : "HelloHelloHello"
member_check = "o" in str1  # Membership Check : True
compare_strings = str1 == str2  # Comparison : False
print(str1[2])            # indexing
print(str1[1:4])        # slicing

# Operator Precedence
# high to low precedence order
'''
Parentheses: ()[]{}
Exponentiation: **
Unary plus and minus: +x, -x, ~x
Multiplication, Division, Floor Division, Modulus: *, /, //, %
Addition and Subtraction: +, -
Bitwise Shifts: <<, >>
Bitwise AND: &
Bitwise XOR: ^
Bitwise OR: |
Comparison Operators: ==, !=, >, <, >=, <=
assignment Operators: =, +=, -=, *=, /=, //=, %=, **=
Identity Operators: is, is not
Membership Operators: in, not in
Logical Operators: and, or, not
'''