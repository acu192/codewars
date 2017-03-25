"""
https://www.codewars.com/kata/gauss-needs-help-sums-of-a-lot-of-numbers/python
"""

def f(n):
    if isinstance(n, int) and n > 0:
        return sum(range(1, n+1))


if __name__ == '__main__':
    print f(1) == 1
    print f(100) == 5050
