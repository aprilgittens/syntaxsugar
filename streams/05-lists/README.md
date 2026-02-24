# Stream 5: Lists

**Status:** [Scheduled](https://youtube.com/live/7QerYXCXsUQ?feature=share)

**Date:** February 26, 2026

**Video:** Coming Soon

## 📋 Overview

One variable, many items. Lists are where Python starts to feel genuinely useful — instead of creating a separate variable for every piece of data, you store everything together in order. You'll learn how to create lists, access items by index, add and remove things, and slice out exactly the chunk of data you need. You'll also hit your first `IndexError`, which is basically a rite of passage.

## 🎯 What You'll Learn

- What a list is and why it's more useful than a bunch of separate variables
- How indexing works (and why Python starts counting at zero)
- How to access, update, add, and remove items
- How to slice a list to grab a subset of items
- How to check if something exists in a list

## ✅ Prerequisites

- Completed Streams 1–6
- Comfortable creating variables and working with basic data types
- Familiar with booleans (`True`/`False`)

## 📚 Topics Covered

### Part 1: What is a List?

- Storing multiple items in one variable
- Creating a list with square brackets `[]`
- Lists are ordered — sequence is preserved
- Lists can hold any data type

### Part 2: Accessing Items

- Zero-based indexing
- Negative indexing
- Using `len()` to count items
- The `IndexError` and what causes it

### Part 3: Modifying Lists

- `.append()` — add to the end
- `.insert()` — add at a specific position
- `.remove()` — remove by value
- `.pop()` — remove by index
- Direct reassignment: `my_list[0] = "new value"`

### Part 4: Slicing

- Grabbing a range of items with `[start:end]`
- Slicing from the start or to the end
- Slices return a new list — the original is unchanged

### Part 5: Membership Check

- Using `in` to check if a value exists in a list
- Returns `True` or `False`


## 💻 Code Examples

All code from this stream is in the [`code/`](code/) folder:

- [creating_lists.py](code/creating_lists.py) — Creating and printing lists
- [indexing.py](code/indexing.py) — Accessing items by index, including negative indexing
- [modify_list.py](code/modify_list.py) — append, insert, remove, pop, and reassignment
- [slicing.py](code/slicing.py) — Slicing lists to get subsets
- [membership.py](code/membership.py) — Using `in` to check for values
- [build_a_list.py](code/build_a_list.py) - Use append to build a list
- [common_mistakes.py](code/common_mistakes.py) — IndexErrors, off-by-one, and other common pitfalls

## 📖 Additional Resources

- [Python Lists Documentation](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [PEP 8 Style Guide](https://pep8.org/)