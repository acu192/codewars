"""
https://www.codewars.com/kata/moving-zeros-to-the-end/python
"""

def move_zeros(array):
    def is_zero(val):
        if isinstance(val, bool): return False
        if isinstance(val, (int, float)): return val == 0
        return False
    a = [val for val in array if not is_zero(val)]
    diff = (len(array) - len(a))
    return a + [0] * diff
