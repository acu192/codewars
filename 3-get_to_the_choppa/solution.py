"""
https://www.codewars.com/kata/get-to-the-choppa/python
"""

from collections import deque


def find_shortest_path(grid, start_node, end_node):
    """
    Searches start to end with a simple BFS.
    """

    q = deque([start_node])

    visited = {start_node: None} # maps visited to previous

    while q:

        here = q.popleft()   # deque is treated like a queue!

        if here is end_node:
            path = []
            while here is not None:
                path.append(here)
                here = visited[here]
            return path[::-1]

        x, y = here.position.x, here.position.y

        neighbors = []

        if x > 0:
            n = grid[x-1][y]
            if n.passable: neighbors.append(n)

        if y > 0:
            n = grid[x][y-1]
            if n.passable: neighbors.append(n)

        if x < len(grid)-1:
            n = grid[x+1][y]
            if n.passable: neighbors.append(n)

        if y < len(grid[0])-1:
            n = grid[x][y+1]
            if n.passable: neighbors.append(n)

        for n in neighbors:
            if n not in visited:
                q.append(n)
                visited[n] = here

    return []

