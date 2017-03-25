"""
https://www.codewars.com/kata/calculator/python
"""

import operator as op


class Calculator(object):

    def __init__(self):
        self.precedence = {'+': 1,
                           '-': 1,
                           '*': 2,
                           '/': 2}
        self.operators  = {'+': op.add,
                           '-': op.sub,
                           '*': op.mul,
                           '/': op.div}

    def to_postfix(self, string):
        stack = []
        postfix = []
        for item in string.split(' '):
            if item in self.precedence:
                pres = self.precedence[item]
                while stack and self.precedence[stack[-1]] >= pres:
                    postfix.append(stack.pop())
                stack.append(item)
            else:
                postfix.append(float(item))
        while stack:
            postfix.append(stack.pop())
        return postfix

    def eval_postfix(self, postfix):
        vals = []
        for item in postfix:
            if item in self.operators:
                b = vals.pop()
                a = vals.pop()
                vals.append(self.operators[item](a, b))
            else:
                vals.append(item)
        return vals[0]

    def evaluate(self, string):
        postfix = self.to_postfix(string)
        answer = self.eval_postfix(postfix)
        return round(answer, 3)


if __name__ == '__main__':
    c = Calculator()
    s = '2 / 2 + 3 * 4 - 6'
    print s
    print c.evaluate(s)

