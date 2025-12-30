# Place inside curly brackets {}
# True and 1 & False and 0 considered same value
# no duplicates allowed
# unordered and unchangeable
# cannot access using index use membership operators(in, not in)

# To access
# 1. use membership
eg_set = {'toyota', 'byd', 'apple', 'x', 'y'}
# cannot add dict and list inside a set 
print('x' in eg_set)

for i in eg_set:
    print(i)

# To add items
eg_set.add('orange')

# To add list
list_to_add = [1, 2, 3]
eg_set.update(list_to_add)
print(eg_set)

# To remove
# .remove() and .discard() take one argument
# .pop() random item removed
eg_set.remove(1)
eg_set.discard(2)
print(eg_set.pop())
print(eg_set)
# eg_set.clear()   # to clear set

# join set uses logical operators to join two or more sets
# union(), update() to join two or more sets