# A list stores multiple values

marks = [ 90 , 80 , 70 , 85]

"""
Lists are:

ordered
mutable
indexed
allow duplicates

"""

# Example:

# marks[0]
# → 90

# You can modify:

# marks[0] = 95
# Now:

# [95, 80, 70, 85]
# This mutability concept becomes extremely important later.

# List Methods
# Important Methods
# append()
# extend()
# insert()
# remove()
# pop()
# clear()
# sort()
# reverse()
# count()
# index()
# copy() 


numbers = [ 1 , 2 , 3 , 4 , 5]
fruits = ["apple" , "banana" , "cherry"]

# 1. append() - Add single element at end
numbers.append(6)
print(numbers)

# 2. extend() - Add multiple elements at end
numbers.extend([7 , 9 , 8])
print(numbers)

# 3. insert() - Add element at specific index
numbers.insert(0, 0)
print(numbers)

# 4. remove() - Remove first occurrence of value
numbers.remove(5)
print(numbers)

# 5. pop() - Remove and return element at index
removed = numbers.pop(0)
print(f"Removed: {removed}, List: {numbers}")

# 6. clear() - Remove all elements
copy_list = numbers.copy()
copy_list.clear()
print(copy_list)

# 7. sort() - Sort in ascending order
unsorted = [5 , 2 , 8 , 1 , 9]
unsorted.sort()
print(unsorted)

# 8. reverse() - Reverse the list
reversed_list = [1, 2, 3, 4, 5]
reversed_list.reverse()
print(reversed_list)

# 9. count() - Count occurrences of element
items = [1, 2, 2, 3, 2, 4]
print(items.count(2))

# 10. index() - Find first index of element
fruits = ["apple", "banana", "cherry", "banana"]
print(fruits.index("banana"))

# 11. copy() - Create shallow copy
original = [1, 2, 3]
duplicate = original.copy()
duplicate.append(4)
print(f"Original: {original}, Duplicate: {duplicate}")

"""
Comparison: With vs Without copy()

❌ WITHOUT copy() - Reference Assignment
python
original = [1, 2, 3]
duplicate = original  # Just a reference, NOT a copy

duplicate.append(4)

print(f"Original: {original}, Duplicate: {duplicate}")
# Output: Original: [1, 2, 3, 4], Duplicate: [1, 2, 3, 4]
# ⚠️ Both changed! They point to the SAME list

Memory visualization:

original ─┐
          ├──> [1, 2, 3, 4]  ← SHARED
duplicate ┘


✅ WITH copy() - Independent Copy
python
original = [1, 2, 3]
duplicate = original.copy()  # True copy

duplicate.append(4)

print(f"Original: {original}, Duplicate: {duplicate}")
# Output: Original: [1, 2, 3], Duplicate: [1, 2, 3, 4]
# ✅ Only duplicate changed! They are SEPARATE lists

Memory visualization:

original ──> [1, 2, 3]
duplicate ──> [1, 2, 3, 4]  ← INDEPENDENT

"""

#  list Comprehension

# Normal Approach
squares =[]

for i in range(1, 6):
    squares.append(i * i)

# List Comprehension
squares = [ i* i for i in range(1 , 6)]
print(squares)

value = [i for i  in range(6) if i % 2 == 0]
print(value)



