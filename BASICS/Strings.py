name = "Mayank"

print(name[0])
print(name[1])

# Python also supports negative indexes.

#  M  a  y  a  n  k
#  0  1  2  3  4  5
# -6 -5 -4 -3 -2 -1

print(name[-1])
print(name[-2])


# Strng Slicing

"""
String Slicing in Python

String slicing extracts a portion of a string using index positions. The syntax is:

python
string[start:end:step]

Basic Syntax

Component	  Meaning
start	      Starting index (inclusive) - defaults to 0
end	          Ending index (exclusive) - defaults to length
step	      Increment between indices - defaults to 1

"""
# Remember:

# start included
# end excluded

print(name[:3])
print(name[2:])
print(name[::-1])

