# use try except to handle errors

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"{e}: Division by zero is not allowed.")


try:
    user_ip = input("Enter an integer: ")
    num = int(user_ip)
except ValueError:
    print(f"'{user_ip}' not a integer: please enter a valid integer.")

# Manually raising an exception
try:
    raise Exception("Manually raised exception for demonstration.")
except Exception as e:
    print(f"{e}: You cannot add different data types directly.")