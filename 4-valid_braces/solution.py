"""
https://www.codewars.com/kata/valid-braces/python
"""

def validBraces(s):
    while True:
        o = s
        s = s.replace('()', '')
        s = s.replace('[]', '')
        s = s.replace('{}', '')
        if o == s:
            break
    return s == ''


if __name__ == '__main__':
    print validBraces( "(){}[]" )
    print not validBraces( "(}" )
    print not validBraces( "[(])" )
    print validBraces( "([{}])" )
