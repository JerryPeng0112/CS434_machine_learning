import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

"""
Logistic Regression Training
"""

LEARNING_RATE = 0.000000001

def main():
	logisticTraining()

def logisticTraining():
	inputData = loadData("./data/usps-4-9-train.csv")

	# load data into matrix X and Y
	X = inputData[:, 0:-1] / 255
	Y = inputData[:, -1]

	trainASE, testASE = batchLearn(X, Y)
	print trainASE
	print testASE
	plotErrors(trainASE, testASE)

def batchLearn(X, Y):
	# get number of independent variables
	n = X.shape[0]
	features = X.shape[1]
	w = np.zeros(features)
	trainASE = []
	testASE = []

	cond = 100
	while(cond != 0):
		gradient = np.zeros(features)
		for i in range(n):
			result = 1 / (1 + np.exp(-1 * np.dot(np.transpose(w), X[i])))
			gradient += np.dot(result - Y[i], X[i])
		w -= LEARNING_RATE * gradient
		cond -= 1
		print cond
		trainASE.append(calcError("./data/usps-4-9-train.csv", w))
		testASE.append(calcError("./data/usps-4-9-test.csv", w))

	return trainASE, testASE

def calcError(path, w):
	inputData = loadData(path)
	X = inputData[:, 0:-1]
	Y = inputData[:, -1]

	n = X.shape[0]
	result = np.dot(X, w)
	count = 0
	idx = 0

	for item in np.nditer(result):
		approx = 0
		if item >= 0.5:
			approx = 1
		if Y[idx] == approx:
			count += 1
		idx += 1

	accuracy = count / (n * 1.0)
	return accuracy

def plotErrors(trainASE, testASE):
	# plot training error
	plt.plot(trainASE, label="training data")
	plt.xlabel('# of Iterations')
	plt.ylabel('Accuracy')
	#plot testing error
	plt.plot(testASE, label="testing data")
	plt.xlabel('# of Iterations')
	plt.ylabel('Accuracy')
	plt.savefig('trainingAccuracy.png')


def loadData(path):
	# load data from file and return data matrix
	file = open(path, "r")
	data = np.genfromtxt(file, delimiter=",")
	return data


if __name__ == "__main__":
	main()
