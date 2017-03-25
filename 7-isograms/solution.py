"""
https://www.codewars.com/kata/isograms/python
"""

from collections import Counter

def is_isogram(string):
    string = string.lower()
    c = Counter(string)
    for k, v in c.items():
        if v > 1:
            return False
    return True

