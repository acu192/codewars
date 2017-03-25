"""
https://www.codewars.com/kata/can-you-get-the-loop/python
"""

def loop_size(node):
    seen = {}
    while node not in seen:
        seen[node] = len(seen)
        node = node.next
    return len(seen) - seen[node]

