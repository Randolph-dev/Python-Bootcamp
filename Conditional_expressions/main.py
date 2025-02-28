# conditional epxression = A one-line shortcut for the if-else statement (ternary operator)
#                         Print or assign one of two values based on a condition
#                         X if conditon else Y

num = 6
a = 6
b = 7
age = 25
temperature = 30
user_role = "admin"

# print("Positive" if num > 0 else "Negative")
# result = "EVEN" if num % 2 else "ODD"
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "Adult" if age >= 18 else "Child"
# weather = "Hot" if temperature > 20 else "Cold"
access_level = "Full access" if user_role == "admin" else "Limited access"

print(access_level)