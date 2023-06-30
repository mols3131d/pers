import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
rc = []
for _ in range(n):
    _ = sys.stdin.readline().split()
    rc.append(_)

print(rc)

def sol():
    visited = deque()
    stack = deque()

    
    move = [[-1, 0], [1, 0], [0, 1], [0 ,-1]]
    
    while :