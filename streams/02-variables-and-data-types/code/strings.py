# String Concatenation
first_name = "April"
last_name = "Gittens"
full_name = first_name + " " + last_name
print(full_name)

# Common mistake - mixing types
age = 35
message = "I am " + age + " years old"  # Error!

# The fix
message = "I am " + str(age) + " years old"
print(message)
