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


if __name__ == '__main__':
    print fusc(0) == 0
    print fusc(1) == 1
    print [fusc(i) for i in xrange(21)] == [0, 1, 1, 2, 1, 3, 2, 3, 1, 4, 3, 5, 2, 5, 3, 4, 1, 5, 4, 7, 3]
    print fusc(85) == 21
