def DBS(x, y):
    choices = [[-2, 0], [0, 2], [2, 0], [0, -2]]
    grap[x][y] = "."
    for choice in choices:
        xn = x + choice[0]
        yn = y + choice[1]
        if 0 <= xn < N1 and 0 <= yn < M1 and grap[xn][yn] == "*":
            DBS(xn, yn)

if __name__ == '__main__':
    N1, M1 = list(map(int, input().split(" ")))
    grap = []
    num = 0
    for i in range(N1):
        lis = list(input())
        grap.append(lis)
    for i in range(N1):
        for j in range(M1):
            if grap[i][j] == "*":
                num += 1
                DBS(i, j)
    print(num)









