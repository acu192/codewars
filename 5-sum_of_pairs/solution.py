"""
https://www.codewars.com/kata/sum-of-pairs/python
"""

def sum_pairs(value_list, target_value):
    s = set()
    for value in value_list:
        req = target_value - value
        if req in s:
            return [req, value]
        s.add(value)
    return None


if __name__ == '__main__':

    l1 = [1, 4, 8, 7, 3, 15]
    l2 = [1, -2, 3, 0, -6, 1]
    l3 = [20, -13, 40]
    l4 = [1, 2, 3, 4, 1, 0]
    l5 = [10, 5, 2, 3, 7, 5]
    l6 = [4, -2, 3, 3, 4]
    l7 = [0, 2, 0]
    l8 = [5, 9, 13, -3]

    print sum_pairs(l1, 8) == [1, 7]
    print sum_pairs(l2, -6) == [0, -6]
    print sum_pairs(l3, -7) == None
    print sum_pairs(l4, 2) == [1, 1]
    print sum_pairs(l5, 10) == [3, 7]
    print sum_pairs(l6, 8) == [4, 4]
    print sum_pairs(l7, 0) == [0, 0]
    print sum_pairs(l8, 10) == [13, -3]
