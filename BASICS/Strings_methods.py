text = "hello world"

# 1. upper() - Convert to uppercase
print(text.upper())
# Output: HELLO WORLD

# 2. lower() - Convert to lowercase
print(text.lower())
# Output: hello world

# 3. capitalize() - First character uppercase, rest lowercase
print(text.capitalize())
# Output: Hello world

# 4. title() - Capitalize first character of each word
print(text.title())
# Output: Hello World

# 5. strip() - Remove leading/trailing whitespace
print(text.strip())
# Output: hello world

# 6. replace() - Replace substring with another
print(text.replace("world", "python"))
# Output: hello python

# 7. split() - Split string into list
print(text.split())
# Output: ['hello', 'world']

# 8. find() - Find index of substring (returns -1 if not found)
print(text.find("world"))
# Output: 6

# 9. count() - Count occurrences of substring
print(text.count("l"))
# Output: 3

# 10. startswith() - Check if string starts with substring
print(text.startswith("hello"))
# Output: True

# 11. endswith() - Check if string ends with substring
print(text.endswith("world"))
# Output: True


text = "  hello world  "
print(text.strip())     # "hello world" (removed spaces)
print(text.lstrip())    # "hello world  " (left strip)
print(text.rstrip())    # "  hello world" (right strip)

text = "hello world"
print(text.replace("world", "python"))      # hello python
print(text.replace("l", "L"))               # heLLo worLd
print(text.replace("l", "L", 1))            # heLlo world (replace only 1st)

text = "hello world python"
print(text.split())          # ['hello', 'world', 'python']
print(text.split("o"))       # ['hell', ' w', 'rld pyth', 'n']

# split with limit
print(text.split(" ", 1))    # ['hello', 'world python']

text = "hello world"
print(text.find("world"))    # 6 (index where "world" starts)
print(text.find("hello"))    # 0
print(text.find("xyz"))      # -1 (not found)

# Alternative: index() - raises error if not found
# print(text.index("xyz"))    # ValueError

print(text.count("hello"))   # 1

text = "hello world"
print(text.startswith("hello"))    # True
print(text.startswith("world"))    # False
print(text.endswith("world"))      # True
print(text.endswith("hello"))      # False

# Check with tuple of options
print(text.startswith(("hi", "hello", "hey")))  # True


