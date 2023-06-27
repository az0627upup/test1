def so():
    N2, M2 = map(int, input().split(" "))
    lis1 = []
    lis2 = []
    lis3 = []
    lis4 = []
    for i in range(2):
        x = list(map(int, input().split(" ")))
        lis1.append(x)
    y = int(input())
    for tr in range(y):
        lis4.append("No")
    for j in range(y):
        z = list(map(int, input().split(" ")))
        lis2.append(z)
    for k in range(y):
        m, n = lis2[k]
        for num in range(M2):
            if (m == lis1[0][num] and n == lis1[1][num]) or (m == lis1[1][num] and n == lis1[0][num]):
                lis3.append(k)
    for c in lis3:
        lis4[c] = "Yes"
    return lis4


if __name__ == '__main__':
    fc = so()
    for i in range(len(fc)):
        print(fc[i])




