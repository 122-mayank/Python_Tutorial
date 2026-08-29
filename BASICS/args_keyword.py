# // Suppose you don't know how many arguments you'll receive

def add(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(add(1,2))
print(add( 1, 2 ,3, 4,5))

# args collect positional elements in to a tuple
