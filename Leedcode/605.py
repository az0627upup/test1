def solution(flower, n):
    for i, num in enumerate(flower):
        if num == 1:
            continue
        if i > 0 and flower[i-1] == 1:       #这里给出了一个判断要i>0，否则列表会out of range
            continue
        if i < len(flower)-1 and flower[i+1] == 1:
            continue
        flower[i] = 1
        n -= 1
    return n <= 0


if __name__ == '__main__':
    print(solution([1, 0, 0, 0, 1, 0, 1], 1))
