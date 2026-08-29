"""
A module is essentially a Python file containing reusable code.

Suppose:

math_utils.py

contains:

def add(a, b):
    return a + b

Another file can import it:

import math_utils

print(math_utils.add(10, 20))

This is the foundation of modular programming.
"""

import math_utils

print(math_utils.add(10 , 20))

