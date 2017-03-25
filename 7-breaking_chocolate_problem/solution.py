"""
https://www.codewars.com/kata/breaking-chocolate-problem/python
"""

def rBreakChocolate(n, m):
    if n <= 1 and m <= 1:
        return 0
    n, m = max(n, m), min(n, m)
    return 1 + rBreakChocolate(n // 2, m) + rBreakChocolate(n // 2 + (n % 2), m)

def breakChocolate(n, m):
    return rBreakChocolate(n, m)
