fruits = ["apple", "banana", "cherry"]

# Add to the end
fruits.append("mango")
# print(fruits) 

# Insert at a specific position
fruits.insert(1, "blueberry")
# print(fruits)

# Update an item
fruits[0] = "avocado"
# print(fruits)

# Remove by value
fruits.remove("banana")
# print(fruits)

# Remove by index (and get the value back)
removed = fruits.pop(0)
# print(removed)
# print(fruits)