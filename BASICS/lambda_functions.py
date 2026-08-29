
# Normal
def square(x):
    return x * x

# Lambda
square = lambda x: x * x
print(square(5))

numbers = [ 1, 2 , 3, 4, 5, 6]
result = map(lambda x:x * x  , numbers)

print(list(result))

ans = filter(lambda x: x % 2 == 0, numbers)
print(list(ans))

# reduce repeatdely combines values



