from numpy import *
import operator


def createDateSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


group, labels = createDateSet()


def classify0(inX, dataSet, labels, k):  # 分类函数
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1))-dataSet  # 分类向量与各个样本向量的差
    sqDiffMat = diffMat**2  # 矩阵中的每个元素的平方
    sqDistances = sqDiffMat.sum(axis=1)  # 矩阵按行将每个元素相加,得到一个向量
    distance = sqDistances**0.5  # 元素开方,得到一个向量
    sortedDistIndicies = distance.argsort()  # 对向量从小到大排序，使用的是索引值,得到一个向量
    classCount = {}
    for i in range(k):  # 将前K个距离最小的点的标签放入classCount中,得到一个向量
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0)+1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(
        1), reverse=True)  # 对classCount进行排序
    return sortedClassCount[0][0]


print(classify0([0, 0], group, labels, 3))


def file2mat(filename):  # 加载文件
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    retMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listfromline = line.split('\t')
        retMat[index, :] = listfromline[0:3]
        classLabelVector.append(int(listfromline[-1]))
        index += 1
    return retMat, classLabelVector


def autoNrom(dataSet):  # 数据归一
    minVal = dataSet.min(0)  # 每列的最小值
    maxVal = dataSet.max(0)  # 每列的最大值
    ranges = maxVal-minVal  # 每列的变化范围
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]  # 计算行数
    normDataSet = dataSet-tile(minVal, (m, 1))
    normDataSet = normDataSet/tile(ranges, (m, 1))
    return normDataSet, ranges, minVal


def datingClassTest():
    hoRatio = 0.5
    retMat, classLabelVector = file2mat("datingTestSet2.txt")
    normDataSet, ranges, minVal = autoNrom(retMat)
    m = normDataSet.shape[0]  # 计算行数
    numTestVecs = int(m*hoRatio)  # 测试集规模
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(
            normDataSet[i, :], normDataSet[numTestVecs:m, :], classLabelVector[numTestVecs:m], 3)
        print("came back:%d,  reale:%d" %
              (classifierResult, classLabelVector[i]))
        if(classifierResult != classLabelVector[i]):
            errorCount += 1
    print(errorCount/float(numTestVecs))


datingClassTest()
