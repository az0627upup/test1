lis1 = []
lis2 = []
N1, M1, N2, M2 = map(int, input().split(" "))
for i in range(N1):
    x = list(map(int, input().split(" ")))
    lis1.append(x)
for j in range(N2):
    y = list(map(int, input().split(" ")))
    lis2.append(y)
res = []
for a in range(N1):
    res.append([])
    for b in range(1):
        lis4 = []
        lis3 = lis1[a]
        for c in range(N2):
            lis4.append(lis2[c][b])
        res_num = sum(map(lambda x, y: x*y, lis3, lis4))
        res[a].append(res_num)
for i in res:
    for j in i:
        print(j, end=' ')
    print()



