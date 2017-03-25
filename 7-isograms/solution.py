"""
https://www.codewars.com/kata/isograms/python
"""

from collections import Counter

def is_isogram(string):
    string = string.lower()
    c = Counter(string)
    for k, v in c.items():
        if v > 1:
            return False
    return True


if __name__ == '__main__':
    print is_isogram("Dermatoglyphics") == True
    print is_isogram("isogram") == True
    print is_isogram("aba") == False
    print is_isogram("moOse") == False
    print is_isogram("isIsogram") == False
    print is_isogram("") == True
