from collections import deque

N, M = list(map(int, "4 6".split(" ")))
map = """101111
101010
101011
111011"""

map = map.split("\n")
map = [[int(j) for j in i] for i in map]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


deq = deque()
deq.append((0, 0))

while deq:
    x, y = deq.popleft()
    print(x, y)
    print()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        print(i, dx[i], dy[i])
        print(bool(0 <= nx <= N - 1))
        print(bool(0 <= ny <= M - 1))
        print()

        if 0 <= nx <= N - 1 and 0 <= ny <= M - 1:
            if map[ny][nx] == 1:
                map[ny][nx] = map[y][x] + 1
                deq.append((nx, ny))

print(map)
