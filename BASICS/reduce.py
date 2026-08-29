# reduce() repeatedly combines values.
# For example:
# 1 × 2 × 3 × 4
# becomes:
# 24

from functools import reduce
result = reduce(lambda a, b: a * b, [1, 2, 3, 4])

print(result)