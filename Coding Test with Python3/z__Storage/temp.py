from collections import deque


def solution(maps):
    n = len(maps[0])
    m = len(maps)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    maps[0][0] = -1
    queue = deque([(0, 0, 1)])

    while queue:
        px, py, pd = queue.popleft()

        if px == m - 1 and py == n - 1:
            return pd

        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]

            if 0 <= nx < m and 0 <= ny < n and maps[nx][ny] == 1:
                maps[ny][nx] = -1
                queue.append((nx, ny, pd + 1))

    return -1
