def decorator(F):
	class w:
		def __init__(self, *args):
			self.args = *args
		def __call__(self, *args):
			F.apply(lambda x: x ** 2, lambda x: x ** 3, *args)
	return w

@decorator
class Fib:
	def __init__(self):
		pass
	def apply(f1, f2, x1, x2):
		print("{} {} {} {}".format(x1, x2, f1(x1), f2(x2)))


def main():
	f = Fib()
	Fib.apply(x1=9, x2=13)
	
if __name__== """__main__""": main()