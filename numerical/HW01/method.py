import abc

class Method(metaclass=abc.ABCMeta):

	def __init__(self, fun, file):
		self.function = fun
		self.err = 0.00000001
		self.counter = 0
		self.rangeLeft, self.rangeRight, self.maximum = self.function.getRange()
		self.delt = self.function.getDel()
		self.file = file

	@abc.abstractmethod
	def execute(self):
		return NotImplemented



class Bisection(Method):

	def __init__(self, fun, file):
		Method.__init__(self, fun, file)

	def execute(self):
		
		while(self.rangeRight < self.maximum):

			left = self.rangeLeft
			right = self.rangeRight
			self.counter = 0

			if(self.function.f(left)*self.function.f(right) < 0):

				while(abs(left-right) >= 2*self.err and self.counter < 100):

					mid = (left + right)/2
					if(self.function.f(mid) == 0):
						break;

					if(self.function.f(left)*self.function.f(mid) < 0):
						right = mid
					else:
						left = mid

					self.counter+=1
				if(self.counter < 100):
					print("Solution = {}, times = {}, err = {:.10f}".format((left + right)/2, self.counter, abs(left-right)), file=self.file)

			self.rangeLeft+=self.delt
			self.rangeRight+=self.delt

class FalsePositionMethod(Method):

	def __init__(self, fun, file):
		Method.__init__(self, fun, file)

	def execute(self):

		while(self.rangeRight < self.maximum):

			left = self.rangeLeft
			right = self.rangeRight
			self.counter = 0

			if(self.function.f(left)*self.function.f(right) < 0):
				
				old = left
				c = right
				# print(old - c)
				while(abs(old - c) >= self.err and self.counter < 100):
					
					old = c
					c = (left*self.function.f(right) - right*self.function.f(left))/(self.function.f(right)-self.function.f(left))

					if(self.function.f(c) == 0):
						break

					if(self.function.f(left)*self.function.f(c) < 0):
						right = c
					else:
						left = c
					
					self.counter += 1
				if(self.counter < 100):
					print("Solution = {}, times = {}, err={:.10f}".format(c, self.counter, abs(left-right)), file=self.file)

			self.rangeLeft += self.delt
			self.rangeRight += self.delt


class ModifyFalsePositionMethod(Method):

	def __init__(self, fun, file):
		Method.__init__(self, fun, file)

	def execute(self):

		while (self.rangeRight < self.maximum):

			left = self.rangeLeft
			right = self.rangeRight
			self.counter = 0

			if(self.function.f(left)*self.function.f(right) < 0):

				old = left
				c = right
				fLeft = self.function.f(left)
				fRight = self.function.f(right)

				while(abs(old - c) >= self.err and self.counter < 100):

					old = c
					c = (left*fRight - right*fLeft)/(fRight - fLeft)
					fC = self.function.f(c)

					if(fLeft * fC < 0):
						right = c
						fLeft /= 2
					else:
						left = c
						fRight /= 2

					self.counter += 1
				if(self.counter < 100):
					print("Solution = {}, times = {}, err = {:.10f}".format(c, self.counter, abs(old-c)), file=self.file)
			
			self.rangeLeft += self.delt
			self.rangeRight += self.delt

class SecantMethod(Method):

	def __init__(self, fun, file):
		Method.__init__(self, fun, file)

	def execute(self):

		while(self.rangeRight < self.maximum):

			left = self.rangeLeft
			right = self.rangeRight
			self.counter = 0

			if(self.function.f(left)*self.function.f(right) < 0):

				while(abs(right - left) >= self.err and self.counter < 100):

					fLeft = self.function.f(left)
					fRight = self.function.f(right)
					c = (left*fRight - right*fLeft)/(fRight - fLeft)
					left = right
					right = c

					self.counter += 1
				if(self.counter < 100):
					print("Solution = {}, times = {}, err = {:.10f}".format(c, self.counter, abs(right - left)), file=self.file)

			self.rangeLeft += self.delt
			self.rangeRight += self.delt

class NewtonsMethod(Method):

	def __init__(self, fun, file):
		Method.__init__(self, fun, file)


	def execute(self):

		while(self.rangeLeft < self.maximum):
			
			self.counter = 0
			x = self.rangeLeft
			delta = 10*self.err
			while(abs(delta) >= self.err and self.counter < 100):
				
				fx = self.function.f(x)
				fdx = self.function.fd(x)
				delta = -fx/fdx

				x = x + delta
				self.counter += 1

			if(self.counter < 100):
				print("Solution = {}, times = {}, err={:.10f}".format(x, self.counter, abs(delta)), file=self.file)
			self.rangeLeft += self.delt


class FixedPointMethod(Method):

	def __init__(self, fun, file):
		Method.__init__(self, fun, file)

	def execute(self):
		
		while(self.rangeRight < self.maximum):
			
			# print("asd")
			self.counter = 0;
			c0 = -1
			xold = c0
			c = -6

			while(abs(xold - c) >= self.err and self.counter < 100):
				
				xold = c
				c = self.function.g(c0)
				c0 = c
				self.counter += 1
				# print(c)

			if(self.counter < 100):
				print("Solution = {}, times = {}, err = {:.10f}".format(c, self.counter, abs(xold-c)), file=self.file)
			# else:
			# 	print("INF")
				
			self.rangeLeft += self.delt
			self.rangeRight += self.delt
