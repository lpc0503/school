import abc
import math

class Function(metaclass=abc.ABCMeta):

	@abc.abstractmethod
	def f(self, x):
		return NotImplemented
	
	@abc.abstractmethod
	def fd(self, x):
		return NotImplemented

	@abc.abstractmethod
	def g(self, x):
		return NotImplemented
	
	@abc.abstractmethod
	def getRange(self):
		return NotImplemented
	
	def getDel(self):
		return NotImplemented


class CommonFunction_First(Function):

	def f(self, x):
		return math.exp(x) - 3*x*math.cos(2*x)-8.3

	def fd(self, x):
		return math.exp(x) - 3*(-2*x*math.sin(2*x)+math.cos(2*x))

	def g(self, x):
		return math.log(3 * x * math.cos(2 * x) + 8.3)

	def getRange(self):
		return (-10, -9, 5.01)
	
	def getDel(self):
		return 1

class CommonFunction_Second(Function):
	
	def f(self, x):
		return math.exp(x*math.sin(x)) - x*math.cos(2*x)-2.8
	
	def fd(self, x):
		return math.exp(x*math.sin(x))*x*math.cos(x) + math.exp(x*math.sin(x))*math.sin(x) + 2*x*math.sin(x) - math.cos(x)

	def g(self, x):
		
		if(math.sin(x) == 0):
			x += 0.01

		return (math.log(x * math.cos(2 * x) + 2.8) / math.sin(x))

	def getRange(self):
		return (-5, -4, 5.01)

	def getDel(self):
		return 0.5

class CustomFunction_First(Function):

	def f(self, x):
		return math.exp(math.cos(2*x)) - (5/12)*x

	def fd(self, x):
		return -2*math.exp(math.cos(2*x))*math.sin(2*x)-(5/12)

	def g(self, x):
		return (5/12)*math.exp(math.cos(2*x))

	def getRange(self):
		return (0.4, 0.7, 3.01)
	
	def getDel(self):
		return 0.3


class CustomFunction_Second(Function):

	def f(self, x):
		return math.exp(math.sin(10*x)) - x**2
	
	def fd(self, x):
		return -2*x + 10*math.exp(math.sin(10*x))*math.cos(10*x)

	def g(self, x):
		# print(x)
		return -math.sqrt(math.exp(math.sin(10*x)))

	def getRange(self):
		return (-1.1, -1.2, 2.1)

	def getDel(self):
		return 0.03

