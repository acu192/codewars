"""
https://www.codewars.com/kata/can-you-get-the-loop/python
"""

def loop_size(node):
    seen = {}
    while node not in seen:
        seen[node] = len(seen)
        node = node.next
    return len(seen) - seen[node]


if __name__ == '__main__':
    # Make a short chain with a loop of 3
    class Node:
        pass
    node1 = Node()
    node2 = Node()
    node3 = Node()
    node4 = Node()
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    print loop_size(node1) == 3

    # Make a longer chain with a loop of 29
    nodes = [Node() for _ in xrange(50)]
    for node, next_node in zip(nodes, nodes[1:]):
        node.next = next_node
    nodes[49].next = nodes[21]
    print loop_size(nodes[0]) == 29
