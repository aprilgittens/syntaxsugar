# This breaks
age = "35"
next_year = age + 1  # Error!

# The fix
age = "35"
next_year = int(age) + 1
print(next_year)
