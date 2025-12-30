# Are placed inside square brackets []
# Ordered and indexed
# Allows duplicate values
# can be made using list() constructor
# list can contain different data types (cannot have set as element)

import random

# To create a list
example_1 = [1, 2, 3, 'apple', 'banana', 2, 3.5, True]

example_2 = list(random.sample(range(1, 20), 5))

print(example_1)
print(example_2, end='\n\n')

# Conversion to list
set_eg = {1, 2, 3, 'apple', 'banana', True}
dict_eg = {'name': 'Ram', 'age': 25, 'city': 'Kathmandu'}
tuple_eg = (1, 2, 3, 'apple', 'banana', False)

list_from_set = list(set_eg)
list_from_dict = list(dict_eg)  # only gives the keys as element for list
list_from_dict_values = list(dict_eg.values())  # gives the values as element for list
list_from_tuple = list(tuple_eg)

print(list_from_set)
print(list_from_dict)
print(list_from_dict_values)
print(list_from_tuple)

# Accessing elements
print("\nAccessing elements:")
example_3 = [1, 2, [3, 4, 5], ('a', 'b', 'c'), {'key1': 'value1', 'key2': 'value2'}]
# cannot have set as element gives error ''TypeError: 'set' object is not subscriptable''
# similary set cannot have list and dict as element because are mutable and unhashable

# access using loop
for item in example_3:
    print(item)

# Indexing[index value(starts at 0)] and Slicing: list[start:stop:step]
print(example_3[0])        # first element
print(example_3[-1])       # last element
print(example_3[2:5])      # slicing
print(example_3[::2])      # skipping elements
print(example_3[::-1])     # reversing the list 
print(example_3[2][1])     # accessing element inside nested list/tuple/dict

# some methods of list
new_list = random.sample(range(1, 100), 10)
new_list.sort()
new_list.reverse()
new_list.pop()
new_list.append(50)
new_list.insert(3, 75) # 3 is index and 75 is value to insert
new_list.remove(50) # removes first occurrence of value 50
new_list.extend([88, 99, 100]) # extends the list by adding multiple values at the end
new_list.count(75) # counts the occurrence of value 75 in the list
new_list.index(75) # returns the index of first occurrence of value 75
new_list.clear() # clears the list


print('lenght of list is ', len(example_3))        # length of the list