# used to store values in key: value pairs
# ordered, changeable
# doesn't allow duplicated
# cannot access using index 

dict_eg = {
    "name": 'ram',
    "age": 23,
    "edu": 'HM',  # gets overwritten by the next "edu" key-value pair
    "edu": 9
    }

dict_new = dict(apple='round', banana='long', pear='oval')
print(dict_new)

# To access
# You can use .get() method or use key from dict
print(dict_eg['age'])
print(dict_eg.get('edu'))
print(dict_eg.items())

# loop
for i in dict_eg:
    print(i)          # gives keys

for i, j in dict_eg.items():
    print(i, j)         # gives key and value 


fruits_tup = ("apple", "mango", "papaya", "pineapple", "cherry")
to_dict = dict(enumerate(fruits_tup, start=1))      # key starts from 1 to 5 for fruits_top

fruits = {"apple", "mango", "papaya"}
keys = ("a", "m", "p")
next_dict = dict(zip(keys, fruits))

# can store dict inside a dict as value
new_dict = {'a': {'a': 1, 'b': 2}, 'b': [22,23], 'ape': {'idiot', 12}}
# similarly list, tuple, set can be stored as value

# To add items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict['runs on'] = 'diesel'
thisdict.update({"color": 'red'})

# TO delete item
# del item
thisdict.pop('color')       # removes color key value 
del thisdict["runs on"]     # removes runs on
# if no parameter passed removes thisdict dictionery


# tuple is hashable so can be used as key in dict
eg = {(1, 2): True, 3: False}
print(eg)


# To change value in dict
dict_eg = {
    "name": 'ram',
    "age": 23,
    "edu": 'HM',  # gets overwritten by the next "edu" key-value pair
    "edu": 9
    }

# to change value in dict
dict_eg['age'] = 60
dict_eg.update({'name': 'shyam'})
print(dict_eg)

# To change keys in dict
dict_eg['identity'] = dict_eg['name']
del dict_eg['name']

# or use
dict_eg['no_years'] = dict_eg.pop('age')
print(dict_eg)