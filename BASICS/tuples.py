coordinates = (10 , 20)

# Like lists, tuples are ordered and indexed.
# But tuples are generally immutable.

# coordinates[0] = 50
# will produce an error

# This gives us an important 
# List
# → mutable

# Tuple
# → immutable

# tuple unpacking 
student = ("Mayank" , 21 , "CSE")
name , age, branch = student

print(name , age , branch , sep = "-")