# use for decision makeing providing conditions

salary = 15000
# if condition statement
if salary > 10000:
    print("You are eligible for a loan")

# if else condition statement
if salary > 20000:
    print("You are eligible for a credit card")
else:
    print("You are not eligible for a credit card")

# nested condition statement
age = 25
if 0 < age < 18:
    print("You are a child")
elif 18 < age < 60:          # you can use multiple elif statements
    print("You are an adult")
else:
    print("You are a senior citizen")