"""
https://www.codewars.com/kata/twisted-sum/python
"""

def compute_sum(n):
    return sum(int(c) for i in range(1, n+1) for c in str(i))
