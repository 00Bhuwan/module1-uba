# written with round brackets
# ordered and unchangable
# access using index

import random
# To Create
eg_tuple = (1, 2, 3, 4, 5)

eg2_tuple = tuple(random.sample(range(1,20),5))

eg3_tuple = (1, 3, [1, 3], 'ram', 12)
# To Access
eg3_tuple[2]        # use index
eg3_tuple[1:3]      # using slicing [start, end, step]
eg3_tuple[::-1]     # reversing
eg3_tuple[2][0]     # access inside within

# using loop to access
for item in eg_tuple:
    print(item)

# Set is unchangeable but there are other way to update it
# 1. can use list then reverse
eg_to_list = list(eg3_tuple)
eg_to_list.append('hari')
eg3_tuple = tuple(eg_to_list)

# 2. add other tuple to existing tuple
new_tup = (123,12)
singel_tup = ('prem',)              # Should have the comma at end for adding a single item
eg3_tuple = eg3_tuple + new_tup + singel_tup

# To delete item
# 1. convert to list remove then convert back
eg_to_list_del = list(eg_tuple)
eg_to_list_del.remove(2)
eg_tuple = tuple(eg_to_list_del)

# To unpack
fruits_tup = ("apple", "mango", "papaya", "pineapple", "cherry")
# either create length of fuits_tup variable or use * 
a, b, c, d, e = fruits_tup

# OR
x, *y, z = fruits_tup
print(x)                # x = apple
print(y)                # y = ['mango', 'papaya', 'pineapple']
print(z)                # z = cherry

# Methods in tuple
print(fruits_tup.count('apple'))
print(fruits_tup.index('papaya'))