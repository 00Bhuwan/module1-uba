# file handling

''' 
file = open('geek.txt', 'r')     # gives FileNotFoundError
print(file) 
'''


# open file if exists if not exist then creates the file with provided name
from pathlib import Path

file_path = Path("make.txt")

if file_path.is_file():
    print("The file exists.")
else:
    file = open('make.txt', 'x') 
    print(file)

to_write = {
    "r": "Read" ,
    "a": "Append",
    "w": "Write",
    "x": "Create",
    "t": "Text mode",
    "b": "Binary mode"
}

f_read = open('make.txt')           # default is reading mode
print(f_read.read())
f_read.close()

# OR use with to open then no need to close the file 
with open('make.txt') as f_reading:
    print(f_reading.read())

# a to append at end of line 
with open("make.txt", 'w') as write_f:
    for key, value in to_write.items():
        write_f.write(f"{key}: {value}\n")

with open('make.txt') as f:
    print(f.read())
# w to overwrite existing content


# to delte file 
# import os
# if os.path.exists("make.txt"):
#   os.remove("make.txt")
# else:
#   print("The file does not exist")


# CSV 
print("\n--work with CSV--\n")
import pandas as pd
import random

dataset = {
   'id': [item for item in range(1,5)],
   'name': ['ram', 'shyam', 'hari', 'gita'],
   'iq': [iq for iq in range(90, 100, 3)]
}
df = pd.DataFrame(dataset)
print(df)


df = pd.read_csv('output.csv')
df['subject'] = ['science', 'math', 'social', 'english']
df.loc[2, 'subject'] = 'nepali'

df = df.drop(['Unnamed: 0'], axis=1)
print(df)
df.to_csv('output.csv')


import csv
with open('output.csv') as csvfile:
    csv_read = csv.reader(csvfile)

    for line in csv_read:
        print(line[3])

with open('output.csv') as newfile:
    csv_reader = csv.DictReader(newfile)

    for line in csv_reader:
        print(line['name'])           # gives onlt name value 
        # unlike .reader method using index value which requires visiting the csv file to find index 
        # here in .DictReader method we can use the Column name to access them


## Json
import json

to_write = {
    "r": "Read" ,
    "a": "Append",
    "w": "Write",
    "x": "Create",
    "t": "Text mode",
    "b": "Binary mode"
} 

# to convert from dict to json
json_eg = json.dumps(to_write)
print("\n--json format--\n", json_eg)

# json converts key-number into string and every dict value in single quotation '' is changed to double ""
# True boolean is changed to true
# cannot allow tuple as a key in json

num_dict = {'name': 'Ramesh', 'age': True, 95: 'iq'}
eg_json = json.dumps(num_dict)
print('gives: ', eg_json)

eg = {(1, 2): True, 3: False}
# eg_to_json = json.dumps(eg)     # gives TypeError: keys must be str, int, float, bool or None, not tuple
print(eg)

# json to dict

# sample_json = {"true": "1", "name": "Ramesh", "age": "12"}
# sample_to_dict = json.loads(sample_json)      # doesn't work doesn;t recognize as json

sample_to_dict = json.loads(eg_json)
print("From json to dict: ", sample_to_dict)