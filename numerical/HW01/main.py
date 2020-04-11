from method import *
from function import *

def printToFile(out, outputFile):
	print(out, file=outputFile)

def execute(fun, outputFile):

	printToFile("----------Bisection----------", outputFile)
	Bisection(fun, outputFile).execute()

	printToFile("----------FalsePosition----------", outputFile)

	FalsePositionMethod(fun, outputFile).execute()

	printToFile("----------ModifyFalsePositoon----------", outputFile)
	ModifyFalsePositionMethod(fun, outputFile).execute()

	printToFile("----------SecantMethod----------", outputFile)
	SecantMethod(fun, outputFile).execute()

	printToFile("----------NewtonsMethod----------", outputFile)
	NewtonsMethod(fun, outputFile).execute()

	printToFile("----------FixedPointMethod----------", outputFile)
	FixedPointMethod(fun, outputFile).execute()


if __name__ == "__main__":
	
	file = open("Function1.txt", "w")
	execute(CommonFunction_First(), file)

	file = open("Function2.txt", "w")
	execute(CommonFunction_Second(), file)
	
	file  = open("Function3.txt", "w")
	execute(CustomFunction_First(), file)

	file = open("Function4.txt", "w")
	execute(CustomFunction_Second(), file)