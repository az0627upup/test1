from math import log
import pandas as pd
import numpy as np
dataSet = pd.read_csv('E:/pythonProject/test1/datasets/ecoli/ecoli.csv', header=1).values.tolist()
data = np.array(dataSet)


def calcInfoEnt(dataSet):
    # code start here
    numEntries = len(dataSet)  # 数据集大小
    labelCounts = {}
    for featVec in dataSet:  #
        currentLabel = featVec[-1]  # 获取分类标签
        if currentLabel not in labelCounts.keys(): labelCounts[currentLabel] = 0  # 字典值不等于0？？？
        labelCounts[currentLabel] += 1  # 每个类中数据个数统计
    infoEnt = 0.0
    for key in labelCounts:  # 信息熵计算
        prob = float(labelCounts[key]) / numEntries
        infoEnt -= prob * log(prob, 2)

    return infoEnt
    # code end here
    # 返回值 infoEnt 为数据集的信息熵，表示为 float 类型


if __name__ == '__main__':
    import  math

    print(math.log(10, math.e))
    print(calcInfoEnt(dataSet))
    # 输出为当前数据集的信息熵

























