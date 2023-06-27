# def permute(lis1):
#     res = []
#
#     def backtrack(lis1, tmp):
#         if not lis1:
#             res.append(tmp)
#             return
#         for i in range(len(lis1)):
#             backtrack(lis1[:i] + lis1[i+1:], tmp + [lis1[i]])
#     backtrack(lis1, [])
#     return res
#
#
# if __name__ == '__main__':
#     nums = ['a', 'b', 'c']
#     print(permute(nums))


# def AllRange(listx, start, end):
#     if start == end:  # 当开始等于结尾时结束
#         for i in listx:
#             print(i, end='')
#         print()
#     for m in range(start, end + 1):
#         listx[m], listx[start] = listx[start], listx[m]
#         AllRange(listx, start + 1, end)
#         listx[m], listx[start] = listx[start], listx[m]
#
#
# list1 = [1, 2, 3]
# AllRange(list1, 0, 2)

import itertools
#
#
class Solution:
    def __init__(self, nums):  # 初始化一个函数
        self.nums = (nums)
        self.result = self.permute(self.nums)  # 自身排列

    def permute(self, nums):
        A = list(itertools.permutations(nums, len(nums)))  # 生成全排列
        for i in range(len(A)):  # 遍历将全排列数顺序数封装为集合
            A[i] = list(A[i])
        return A


if __name__ == '__main__':
    n = int(input("请输入一个数"))
    nums = [i for i in range(1, n + 1)]
    solution = Solution(nums)  # 传入列表
    Lst = solution.result  #
    print(Lst)

