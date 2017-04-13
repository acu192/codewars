"""
https://www.codewars.com/kata/magnet-particules-in-boxes
"""

from math import pow


def doubles(maxk, maxn):
    return sum(sum(pow(n+1, -2*k) for n in range(1, maxn+1))/k for k in range(1, maxk+1))


def assertFuzzyEquals(actual, expected, msg=""):
    merr = 1e-6
    inrange = abs(actual - expected) <= merr
    if (inrange == False):
        msg = "At 1e-6: Expected value must be {:0.6f} but got {:0.6f}"
        msg = msg.format(expected, actual)
        return msg
    return True


print assertFuzzyEquals(doubles(1, 10), 0.5580321939764581)
print assertFuzzyEquals(doubles(10, 1000), 0.6921486500921933)
print assertFuzzyEquals(doubles(10, 10000), 0.6930471674194457)
print assertFuzzyEquals(doubles(20, 10000), 0.6930471955575918)
