"""
https://www.codewars.com/kata/escape-the-mines/python
"""

from collections import deque


def solve(map, miner, exit):
    """
    Searches start to end with a simple BFS.
    """

    miner = (miner['x'], miner['y'])
    exit = (exit['x'], exit['y'])

    q = deque([miner])

    visited = {miner: (None, None)} # maps visited to (prev, direction)

    while q:

        here = q.popleft()   # deque is treated like a queue!

        if here == exit:
            path = []
            here, direction = visited[here]
            while here is not None:
                path.append(direction)
                here, direction = visited[here]
            return path[::-1]

        x, y = here

        neighbors = []

        if x > 0:
            n = (x-1, y)
            if map[x-1][y]: neighbors.append((n, 'left'))

        if y > 0:
            n = (x, y-1)
            if map[x][y-1]: neighbors.append((n, 'up'))

        if x < len(map)-1:
            n = (x+1, y)
            if map[x+1][y]: neighbors.append((n, 'right'))

        if y < len(map[0])-1:
            n = (x, y+1)
            if map[x][y+1]: neighbors.append((n, 'down'))

        for n, direction in neighbors:
            if n not in visited:
                q.append(n)
                visited[n] = (here, direction)

    return []


if __name__ == '__main__':
    # Should return an empty array, since we're already at the goal
    minemap = [[True]]
    print solve(minemap, {'x':0,'y':0}, {'x':0,'y':0}) == []

    # Should return the only correct move
    minemap = [[True, False],
               [True, True]]
    print solve(minemap, {'x':0,'y':0}, {'x':1,'y':0}) == ['right']

    # Should return the only moves necessary
    print solve(minemap, {'x':0,'y':0}, {'x':1,'y':1}) == ['right', 'down']

    # Should return a chain of moves to the right
    minemap = [[True], [True], [True], [True]]
    print solve(minemap, {'x':0,'y':0}, {'x':3,'y':0}) == ['right', 'right', 'right']

    # Should return a chain of moves to the left
    print solve(minemap, {'x':3,'y':0}, {'x':0,'y':0}) == ['left', 'left', 'left']

    # Should return the right sequence of moves'
    minemap = [[True, True, True],
               [False, False, True],
               [True, True, True]]
    print solve(minemap, {'x':0,'y':0}, {'x':2,'y':0}) == ['down', 'down', 'right', 'right', 'up', 'up']
