def merge_sort(a, b):
    i = j = 0
    c = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i = i+1
        else:
            c.append(b[j])
            j = j+1

    if i == len(a):
        for x in b[j:]:
            c.append(x)
    else:
        for y in a[i:]:
            c.append(y)
    return c


def merge_st(lists):
    if len(lists) <= 1:
        return lists
    x = len(lists)//2
    left = merge_st(lists[:x])
    right = merge_st(lists[x:])
    return merge_sort(left, right)


if __name__ == '__main__':
    lis1 = list(map(int, input().split(" ")))
    print(merge_st(lis1))


