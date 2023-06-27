def eraseOverlapIntervals(intervals) -> int:
    if len(intervals) == 0:
        return 0
    count = 0
    def takesecond(lis):
        return lis[1]
    intervals.sort(key=takesecond)
    pv = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] < pv:
            count += 1
        else:
            pv = intervals[i][1]
    return count



if __name__ == '__main__':
    x = int(input())
    lis = []
    for i in range(x):
        y = list(map(int, input().split(",")))
        lis.append(y)
    fc = eraseOverlapIntervals(lis)
    print(fc)


