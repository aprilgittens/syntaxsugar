# Quotes Around Numbers

age = "25"  # This is a string, not a number!
age = 25    # This is correct for math

# Forgetting Quotes on Strings

name = Alex  # Error! Python thinks Alex is a variable
name = "Alex"  # Correct

# Using Reserved Words

print = "hello"  # Bad! Don't overwrite built-in functions

# Type Mixing

"5" + 5  # Error!
5 + 5    # Works
"5" + "5"  # Works but gives "55", not 10