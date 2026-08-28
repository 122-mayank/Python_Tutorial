# name = input("Enter your name:")
# print(name)

# # By default the input is returning the string type data tyep
# print(type(name))

# we have to typecast to take input values

# Very important point
# input() always returns a string.

# age = int(input("Enter the number "))
# print(age)
# print(age + 5)
# print(type(age))


# Taking Multiple inputs
# print("Enter two numbers ")
# a , b = input().split()

# print(a)
# print(b)
# print(type(a))
# print(type(b))


# as a integer
print("Enter the two numbers ")
a , b = map(int, input().split())

print(a)
print(b)
print(type(a))
print(type(b))