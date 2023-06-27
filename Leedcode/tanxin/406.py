def solution(people):
    res = []
    peo = sorted(people, key=lambda x: (-x[0], x[1]))
    for p in peo:
        if len(res) <= p[1]:
            res.append(p)
        elif len(res) > p[1]:
            res.insert(p[1], p)
    return res


if __name__ == '__main__':
    x = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    print(solution(x))
