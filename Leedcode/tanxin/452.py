def get_non_overlap_intervals(intervals) -> int:
    """ 求不重叠区间个数 """
    result = 1
    _intervals = sorted(intervals, key=lambda x: x[1])
    # 第一个区间的终点
    end_position = _intervals[0][1]
    for interval in _intervals[1:]:
        # 不重叠区间：区间起点大于区间终点
        if interval[0] > end_position:
            result += 1
            end_position = interval[1]
    return result


def solution(points):
    count = 1
    def getsecond(elem):
        return elem[1]
    points.sort(key=getsecond)
    end_position = points[0][1]
    for i in range(1, len(points)):
        if points[i][0] > end_position:
            count += 1
            end_position = points[i][1]
    return count


def solutionabs(points):
    count = 1
    points.sort(key=lambda x: x[1])
    end_position = points[0][1]
    for i in range(1, len(points)):
        if points[i][0] > end_position:
            count += 1
            end_position = points[i][1]
    return count
if __name__ == '__main__':
    # fc = get_non_overlap_intervals([[10, 16], [2, 8], [1, 6], [7, 12]])
    # fc = solution([[10, 16], [2, 8], [1, 6], [7, 12]])
    fc = solutionabs([[10, 16], [2, 8], [1, 6], [7, 12]])
    print(fc)
