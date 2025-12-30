# make it easy to create, modify list

eg_list = []
for i in range(8):
    eg_list.append(i**2)
print(eg_list)

# above creating utilize more time now using list comprehension
# Syntax: newlist = [expression for item in iterable if condition == True]

eg_comp = [i ** 2 for i in range(8)]
print(eg_comp)

new_eg_comp = [i ** 2 for i in range(8) if i % 2 == 0]
print(new_eg_comp)

neg_comp = [i ** 2 if i % 2 == 0 else 'hi' for i in range(8)]
print(neg_comp)

# Dictionery Comprehension
print('\n')
power_of = {integer: 2 ** integer for integer in range(1,10) }
print(power_of)

power_of = {integer: 2 ** integer if integer % 2 == 0 else 'hi' for integer in range(1,10) }
print(power_of)

fruits = ['apple', 'cherry', 'banana', 'pear']
fruits_dict = {fruit.upper(): len(fruit) for fruit in fruits}
print(fruits_dict)

prices = [100, 200, 300, 400]
new_fruits = {fruit: value for fruit, value in zip(fruits, prices)}
print(new_fruits)