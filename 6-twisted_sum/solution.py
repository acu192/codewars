"""
https://www.codewars.com/kata/twisted-sum/python
"""

def compute_sum(n):
    return sum(int(c) for i in range(1, n+1) for c in str(i))


if __name__ == '__main__':

    cases = ((1, 1), (2, 3), (3, 6), (4, 10), (10, 46))

    for inp, res in cases:
        print compute_sum(inp) == res
