def check(f, fc, a):
    final = []
    for i in range(a):
        b = [a1[i] for a1 in fc]
        result = 0
        for j in range(a):
            result += f[j] * b[j]
        final.append(result)
    return final.index(max(final))


if __name__ == '__main__':
    a = 3
    f = [0.1, 0.1, 0.1]
    fc = [[0.3, 0.2, 0.1], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]]
    check(f, fc, a)












