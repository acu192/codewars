"""
https://www.codewars.com/kata/iq-test/python
"""

from collections import defaultdict

def iq_test(numbers):
    lst = [int(s) for s in numbers.split(" ")]
    d = defaultdict(list)
    for item in lst:
        d[item%2].append(item)
    for oddness, items in d.iteritems():
        if len(items) == 1:
            return lst.index(items[0]) + 1


if __name__ == '__main__':
    print iq_test("2 4 7 8 10") == 3
    print iq_test("1 2 2") == 1
    print iq_test("1 2 1 1") == 2
