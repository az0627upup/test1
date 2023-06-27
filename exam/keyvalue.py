import operator
import random
import numpy as np
def solution():
    distances = []
    labels = []
    for i in range(400):
        k = int(random.uniform(0, 3))
        labels.append(k)
    for i in range(400):
        j = int(random.uniform(0, 1000))
        distances.append(j)
    dis = np.array(distances)
    sorteddis = dis.argsort()
    classcount = {}
    for i in range(40):
        labelname = labels[sorteddis[i]]
        classcount[labelname] = classcount.get(labelname, 0)+1
    sortedclasscount = sorted(classcount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedclasscount[0][0]

if __name__ == '__main__':
    sc = solution()
    print(sc)

