# cost = [0]
# weight = [0]
# n, v = map(int, input().split())
# for i in range(n):
#     c, w = map(int, input().split())
#     cost.append(c)
#     weight.append(w)
# dp = [[0 for i in range(v + 1)] for j in range(n + 1)]
# for a in range(1, n+1):
#     for b in range(1, v+1):
#         if b < cost[a]:
#             dp[a][b] = dp[a-1][b]
#         else:
#             dp[a][b] = max(dp[a-1][b-cost[a]] + weight[a], dp[a-1][b])
# print(dp[n][v])

cost = [0]
weight = [0]
n, v = map(int, input().split())
for i in range(n):
    cos, wei = map(int, input().split())
    cost.append(cos)
    weight.append(wei)
dp = [0 for m in range(v+1)]
for i in range(1, n+1):
    for j in range(v, 0, -1):  # 这里采用逆序遍历的原因是当j-cost[i]表示的是当除去第i件物品后背包容量为j-cost[i]时背包所能装的最大质量，而逆序的话就能保证前面背包的最大质量
        if j >= cost[i]:       # 为i-1时的质量，即不包括第i件物品时的最大质量。
            dp[j] = max(dp[j], dp[j-cost[i]]+weight[i])
print(dp[v])


