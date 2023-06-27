import string
import matplotlib.pyplot as plt
import math


def draw_from_dict(dicdata, RANGE, heng=0):
    # dicdata：字典的数据。
    # RANGE：截取显示的字典的长度。
    # heng=0，代表条状图的柱子是竖直向上的。heng=1，代表柱子是横向的。考虑到文字是从左到右的，让柱子横向排列更容易观察坐标轴。
    by_value = sorted(dicdata.items(), key=lambda item: item[0], reverse=False)
    x = []
    y = []
    plt.xlabel("Sequential letters")
    plt.ylabel("Probability of occurrence of each letter")
    plt.title("Character probability statistics")
    for xx, yy in zip(dicdata.keys(), dicdata.values()):
        # plt.text(xx, yy + 0.1, str(yy), ha='center')
        if yy != 0:
            plt.text(xx, yy, '%.3f' % yy, ha='center', va='bottom', fontsize=5)
    for d in by_value:
        x.append(d[0])
        y.append(d[1])
    if heng == 0:
        plt.bar(x[0:RANGE], y[0:RANGE])
        plt.show()
        return
    elif heng == 1:
        plt.barh(x[0:RANGE], y[0:RANGE])
        plt.show()
        return
    else:
        return "heng的值仅为0或1！"


def countLetters(string):
    s_count = 0
    for i in s:
        if i.isalpha():
            s_count += 1
    print('字母的个数有：', s_count, '个')
    return s_count


s = 'Love is a set of emotions and behaviors characterized by intimacy, passion, and commitment. It involves care, ' \
    'closeness, protectiveness, attraction, affection, and trust. Love can vary in intensity and can change over ' \
    'time. It is associated with a range of positive emotions, including happiness, excitement, life satisfaction, ' \
    'and euphoria, but it can also result in negative emotions such as jealousy and stress. '
letterSum = countLetters(s)
print(letterSum)
asciiAll = string.ascii_lowercase + string.ascii_uppercase
dict3 = {key: 0.0 for key in asciiAll}
for x in s:
    if x.isalpha():
        dict3[x] = round(s.count(x) / letterSum, 6)

for i in sorted(dict3):
    print((i, dict3[i]), end="\n")
sum1 = 0
for i in dict3:
    if dict3[i] != 0:
        sum1 += dict3[i] * (math.log(1 / (dict3[i]), 2))

print('计算出的熵是', round(sum1, 4))

draw_from_dict(dict3, 52, 0)






