# Charles Thomas Wallace Truscott Watters
def W(F):
	class wrap:
		def __init__(self, *args):
			self.wrapper = F(*args)
		def square(self, n):
			return self.wrapper.square(n)
		def cube(self, n):
			return self.wrapper.cube(n)
	return wrap
	
@W
class Poly:
	def __init__(self, square, cube):
		self.square = square
		self.cube = cube
def Charles():
	p = Poly(lambda x: x ** 2, lambda x: x ** 3)
	print(p.square(16), p.cube(16))
Charles()