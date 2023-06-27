def solution(s):
    d = {}
    result = []
    for i in range(len(s)):
        d[s[i]] = i                         #此处的列表记录的是元素s[i]的最后出现的位置
    start = 0
    end = 0
    for j in range(len(s)):
        end = max(end, d[s[j]])
        if j == end:
            result.append(end - start + 1)
            start = end + 1
    return result


if __name__ == '__main__':
    fc = solution("ababcbacadefegdehijhklij")
    print(fc)


