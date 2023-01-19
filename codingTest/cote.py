import sys
N, M, R = map(int, sys.stdin.readline().split())

tree = {}

for i in range(1, M+1):
    
    tree[i] = []
    
    u, v = map(int, sys.stdin.readline().split())
    if u in tree.keys():
        tree[u].append(v)
    else:
        tree[u] = [v]

print(tree)


def dfs(graph, cur=1, visited=[]):
    visited.append(cur)

    for i in graph[cur] :
        if i not in visited:
            dfs(graph,i,visited)
    
    return visited

print(dfs(tree))