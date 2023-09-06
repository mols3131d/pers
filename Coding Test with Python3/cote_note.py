from collections import deque

n = int(input())
a, b = list(map(int, input().split()))
m = int(input())

graph = {}
for i in range(m):
    graph[i+1] = []

for i in range(m):
    x, y = list(map(int, input().split()))
    graph[x] += [y]
    
print(graph)