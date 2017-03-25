"""
https://www.codewars.com/kata/bit-counting/python
"""

def countBits(n):
    i = 0
    while n > 0:
        if n & 1:
            i += 1
        n >>= 1
    return i

