import numpy as np
from numpy.linalg import eig

def PCA(dataSet, targetFeatures):
    if len(dataSet) == 0:
        return dataSet
    elif len(dataSet[0]) == 0:
        return dataSet
    featureSize = len(dataSet[0])
    for colIdx in range(featureSize):
        dataSet[:,colIdx] = dataSet[:,colIdx] - np.mean(dataSet[:,colIdx])
    covarianceMatrix = np.zeros((featureSize, featureSize))
    for x in range(featureSize):
        for y in range(featureSize):
            covarianceMatrix[x,y] = np.dot(dataSet[:, x], dataSet[:, y])/(len(dataSet[:,x]) - 1)
    (eigVals, eigVecs) = eig(covarianceMatrix)
    indecesToUse = list(reversed([i[0] for i in sorted(enumerate(eigVals), key = lambda x:x[1])]))
    indecesToUse = indecesToUse[:targetFeatures]
    return np.dot(dataSet, eigVecs[:,indecesToUse])




data = np.asarray([
    [2.5, 2.4],
    [.5, .7],
    [2.2, 2.9],
    [1.9, 2.2],
    [3.1, 3.0],
    [2.3, 2.7],
    [2.0, 1.6],
    [1.0, 1.1],
    [1.5, 1.6],
    [1.2, 0.9]
])
print(PCA(data, 1))