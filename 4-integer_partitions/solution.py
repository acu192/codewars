"""
https://www.codewars.com/kata/getting-along-with-integer-partitions/python
"""

ENUM_CACHE = {}


def enum(n):

    if n < 1:
        raise Exception("invalid input to enum")

    if n in ENUM_CACHE:
        return ENUM_CACHE[n]

    parts = {(n,)}
    for i in range(1, n):
        sub_enum = enum(n-i)
        for sub_part in sub_enum:
            part = tuple(sorted(sub_part + (i,)))
            parts.add(part)

    ENUM_CACHE[n] = parts
    return parts


def part(n):

    prods = set()

    for part in enum(n):
        prod = reduce(lambda a,b: a*b, part)
        prods.add(prod)

    n = len(prods)
    prods = sorted(list(prods))

    range = prods[-1] - prods[0]
    avg = 1.0 * sum(prods) / n
    median = prods[n/2] if ((n % 2) == 1) else (prods[n/2-1] + prods[n/2]) / 2.0

    return "Range: {} Average: {:.2f} Median: {:.2f}".format(range, avg, median)

