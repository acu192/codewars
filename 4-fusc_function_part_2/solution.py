"""
https://www.codewars.com/kata/the-fusc-function-part-2/python
"""

# import sys
# sys.setrecursionlimit(10000)


# def F(n, a, b):
#     if n == 0:
#         return b
#     if n == 1:
#         return a+b
#     if (n % 2) == 0:
#         return F(n//2, a+b, b)
#     else:
#         return F(n//2, a, a+b)


def F(n, a, b):
    while n >= 2:
        if (n % 2) == 0:
            a, b = a+b, b
        else:
            a, b = a, a+b
        n //= 2

    if n == 0:
        return b
    else:
        return a+b


def fusc(n):
    if n <= 1:
        return n
    while (n % 2) == 0:
        n //= 2
    return F(n // 2, 1, 1)


if __name__ == '__main__':
    print fusc(0) == 0
    print fusc(1) == 1
    print fusc((1<<1000) + 1) == 1001
    print fusc((1<<1000) - 1) == 1000
    print fusc((1<<1000) + 5) == 2996
    print fusc((1<<1000) + 21) == 7973
