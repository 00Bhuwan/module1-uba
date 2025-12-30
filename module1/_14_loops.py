# for loops
for i in range(5):
    print(i)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for x in fruits[0]:
    print(x)

dict_items = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in dict_items.items():
    print(f"{key}: {value}")

# while loops
count = 0
while count < 5:
    print(count)
    count += 1

# infinite loop with break
print('infinite loop with break')
num = 0
while True:
    if num == 3:
        break
    print(num)
    num += 1

# continue statement
print('continue statement')
for i in range(5):
    if i == 2:
        continue   # skips for i==2 then continue
    print(i)

# nested loops
print('nested loops')
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# use for decision making providing conditions
salary = 15000
# if condition statement
if salary > 10000:
    print("You are eligible for a loan")
# if else condition statement
if salary > 20000:
    print("You are eligible for a credit card")
else:
    print("You are not eligible for a credit card")
