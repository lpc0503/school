import numpy as np
import random
import time

file = None

tFile = open("time.txt", "w")
test = [2, 4, 10]
N = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 500, 1000, 2000, 5000]

def printToFile(string, end='\n', outFile=file):

	if(outFile == tFile):
		print(string, file=outFile, end=end)
	else:
		print(string, file=file, end= end)

def printArr(arr):

	for i in range(len(arr)):
		for j in range(len(arr[i])):
			printToFile("{} ".format(arr[i][j]), end='')
		printToFile("")
	printToFile("")

def printAns(X):

	printToFile("Ans")
	printToFile("=========================")
	for i in range(len(X)):
		for j in range(len(X[i])):
			printToFile("X_{}: {}".format(i, X[i][j]))

	printToFile("")

def rand(n):

	tmp = []
	tmp_ans = []
	for i in range(n):
		new = []
		new_ans = []
		for j in range(n):
			new.append(random.randint(-10, 10))
		tmp.append(new)

		new_ans.append(random.randint(-50, 50))
		tmp_ans.append(new_ans)

	return tmp, tmp_ans


def gauss(A, b):
	return np.linalg.solve(A, b)

def check(A, b, X):

	t = A.dot(X)
	t = t.astype(int)

	print(b)
	print(t)

	print("=======\n")

	if (t == b).any():
		return True
	else:
		return False

def main():

	global file

	s = "output_"

	printToFile("HW02")

	count = 0
	for num in N:

		filename = s + str(num) + ".txt"
		file = open(filename, "w")

		printToFile("--------------------------------------------------------------------")
		printToFile("                              n = {}                                ".format(num))
		printToFile("--------------------------------------------------------------------\n")	
				
		A, b = rand(num)
		A = np.asarray(A)
		b = np.asarray(b)

		tmp_b = np.reshape(b, (1, num))
		printToFile("random number A")
		printArr(A)
		printToFile("random number b")
		printArr(tmp_b)


		tStart = time.time()
		X = gauss(A, b)
		tEnd = time.time()

		printToFile("{:.6f}".format(tEnd-tStart), outFile=tFile)


		printAns(X)


		printToFile("check")

		printToFile("===============================")
		if(check(A, b, X)):
			count += 1
			printToFile("success")
		else:
			printToFile("wrong")

	print(count)


if __name__ == "__main__":
	main()
