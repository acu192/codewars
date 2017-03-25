"""
https://www.codewars.com/kata/sum-of-pairs/python
"""

def sum_pairs(value_list, target_value):
    s = set()
    for value in value_list:
        req = target_value - value
        if req in s:
            return [req, value]
        s.add(value)
    return None
