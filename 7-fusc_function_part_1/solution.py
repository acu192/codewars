"""
https://www.codewars.com/kata/the-fusc-function-part-1/python
"""


def fusc(n):
    if n <= 1:
        return n

    if (n % 2) == 0:  # even
        return fusc(n//2)
    else:             # odd
        return fusc(n//2) + fusc(n//2+1)
