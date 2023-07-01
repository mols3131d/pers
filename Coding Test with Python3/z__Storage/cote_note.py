import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
rc = []

for _ in range(n):
    _ = sys.stdin.readline().split()
    rc.append(_)


print(rc)


def sol(n, m, rows):
    move = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    visited = [[False] * m for i in range(n)]
    queue = deque((0, 0))

    while queue:
        rc = queue.pop()

        for i in move:
            moved_y = rc[1] + i[1]
            moved_x = rc[0] + i[0]

            if not visited[moved_x][moved_y]:
                queue.append(moved_y, moved_x)
                visited[moved_y][moved_x] = True
