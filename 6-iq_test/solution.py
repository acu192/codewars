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
