def solution():
    str = input().split(" ")
    m = len(str)
    tag = []
    ress = set()
    for i in range(m):
        res = set(str[i])
        x = res.isdisjoint(ress)
        if x == False:
            for j in range(i):
                if res.issubset(set(str[j])) or set(str[j]).issubset(res):
                    tag.append([i])
        ress = ress | res
    if len(ress) != 10:
        return -1
    y = len(str)-len(tag)
    return y


if __name__ == '__main__':
   k = solution()
   print(k)