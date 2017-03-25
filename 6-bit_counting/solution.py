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


if __name__ == '__main__':
    print countBits(0) == 0
    print countBits(4) == 1
    print countBits(7) == 3
    print countBits(9) == 2
    print countBits(10) == 2
