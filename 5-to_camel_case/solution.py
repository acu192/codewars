"""
https://www.codewars.com/kata/convert-string-to-camel-case/python
"""

def to_camel_case(text):
    if not text: return ''
    l = []
    next = text[0].isupper()
    for c in text:
        if c in '_-':
            next = True
        else:
            if next:
                l.append(c.upper())
                next = False
            else:
                l.append(c)
    return ''.join(l)


if __name__ == '__main__':

    print to_camel_case('') == ''
    print to_camel_case("the_stealth_warrior") == "theStealthWarrior"
    print to_camel_case("The-Stealth-Warrior") == "TheStealthWarrior"
    print to_camel_case("A-B-C") == "ABC"
