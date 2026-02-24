# Off-By-One
colors = ["red", "green", "blue"]

print(colors[1])  # green — NOT red!
print(colors[0])  # red — the first item is always index 0

# Index Out of Range
colors = ["red", "green", "blue"]  # 3 items, valid indexes: 0, 1, 2

print(colors[3])  # IndexError! There is no index 3
print(colors[-1]) # This works — negative indexing starts from the end, so -1 is the last item (blue)

# Confusing .remove() and .pop()
nums = [10, 20, 30]

nums.remove(20)  # Removes by VALUE — looks for 20 in the list
nums.pop(0)      # Removes by INDEX — removes whatever is at position 0

# Common mistake: using .remove() with an index
nums.remove(0)   # Tries to find the value 0 — might cause a ValueError!

# Slices don't change the original list
numbers = [1, 2, 3, 4, 5]
first_two = numbers[:2]

print(first_two)  # [1, 2]
print(numbers)    # [1, 2, 3, 4, 5] — unchanged

# Printing a list vs. an item
pets = ["dog", "cat", "fish"]

print(pets)     # ['dog', 'cat', 'fish'] — the whole list with brackets
print(pets[0])  # dog — just the item, no brackets