def newton(a, b, c):
    x0 = 0.01
    e = 1e-6       #此处即为e为1x10的-6次方
    x_n = x0 - ((x0 ** 3 + a * x0 ** 2 + b * x0 - c)/(3 * x0 ** 2 + 2 * a * x0 + b))
    while abs(x_n - x0) > e:
        x0 = x_n
        x_n = x0 - ((x0 ** 3 + a * x0 ** 2 + b * x0 - c)/(3 * x0 ** 2 + 2 * a * x0 + b))
    return x_n

if __name__ == '__main__':
    x = int(input())
    lis1 = []
    outputs = []
    for i in range(x):
        m = list(map(int, input().split(" ")))
        lis1.append(m)
    for j in range(x):
        outputs.append(newton(lis1[j][0], lis1[j][1], lis1[j][2]))
    for k in range(len(outputs)):
        print(outputs[k])
























