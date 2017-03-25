"""
https://www.codewars.com/kata/a-chain-adding-function/python
"""

class Int(int):

    def __init__(self, val):
        super(Int).__init__()

    def __call__(self, other):
        return Int(self + other)

def add(val):
    return Int(val)

