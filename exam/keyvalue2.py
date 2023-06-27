def solution(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    count = {v: k for k, v in count.items()}
    print(count)
    return count[1]
if __name__ == '__main__':
    c = [k for k in input().split()]
    fc = solution(c)
    print(fc)

    """
    实现的功能是从控制台输入一行数字，用空格隔开，输入的字符中仅有一个字符个数为1，其他不限制，求输出其中字符个数为1的字符
    """