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


if __name__ == '__main__':

    print add(1)(2) == 3

    print add(1)(2)(3) == 6
    print add(1)(2)(3)(4) == 10
    print add(1)(2)(3)(4)(5) == 15

    print add(1) == 1

    addTwo = add(2)
    print addTwo == 2
    print addTwo + 5 == 7
    print addTwo(3) == 5
    print addTwo(3)(5) == 10
