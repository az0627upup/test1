# n, v = map(int, input().split())
# # w为物品价值，c为物品体积（花费）
# w, cost = [0], [0]
# for i in range(n):
#     cur_c, cur_w = map(int, input().split())
#     w += [cur_w]*2
#     cost += [cur_c]*2
#
# n = len(w)-1
#
# dp = [0 for j in range(v+1)]
# for i in range(1, n+1):
#     for j in range(v, 0, -1):
#         if j >= cost[i]:
#             dp[j] = max(dp[j], dp[j-cost[i]]+w[i])
# print(dp[v])


n, v = map(int, input().split())
cost = [0]
weight = [0]
for i in range(n):
    cos, wei, num = map(int, input().split())
    cost += [cos]*num
    weight += [wei]*num
n = len(weight)-1
dp = [0 for i in range(v+1)]
for i in range(1, n+1):
    for j in range(v, 0, -1):
        if j >= cost[i]:
            dp[j] = max(dp[j], dp[j-cost[i]]+weight[i])
print(dp[v])

