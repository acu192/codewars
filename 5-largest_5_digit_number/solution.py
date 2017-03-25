"""
https://www.codewars.com/kata/largest-5-digit-number-in-a-series/python
"""

def solution(digits):
    vals = [int(digits[i:i+5]) for i in range(len(digits)-4)]
    return max(vals)
