def solution(a):
    sum = 10
    if a > 10:
        sum = sum + 1
    elif a < 22:
        sum = 20
    c = 10
    return sum


def solutionsc(b):
    sum1 = 10
    if b > 10:
        sum1 = sum1 + 1
    if b < 20:
        sum1 = sum1 + 20
    c = 10
    return sum1


if __name__ == '__main__':
    print(solution(11))
    print(solutionsc(11))

"""
这里主要说明的是当if语句的条件成立时，elif里面的语句就不会再执行，
而再if后面再加个if语句之后第一个if条件成立之后第二个if同样会执行。
"""









