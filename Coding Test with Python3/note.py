N = int(input())

cost = []
for _ in range(N):
    cost.append(list(map(int, input().split(" "))))

dp = [[0, 0, 0] for _ in range(N)]

c = [0, 1, 2]

for j in range(len(c)):
    dp[0][j] = cost[0][j]

for i in range(1, N):
    for j in range(len(c)):
        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j - 2]) + cost[i][j]


print(min(dp[-1]))
