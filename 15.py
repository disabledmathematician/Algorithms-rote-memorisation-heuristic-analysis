class Fibonacci:
	def __init__(self, n, memo):
		self.n = n
		self.memo = {}
	def Fibonacci_Iter(self):
		a, b = 0, 1
		for x in range(self.n):
			a, b = b, a + b
			print(b)
	def Fibonacci_Recur(self, n):
		if self.memo == None:
			self.memo = {}
		if n == 0 or n == 1:
			return 1
		try:
			return self.memo[n]
		except KeyError:
			f = self.Fibonacci_Recur(n - 1) + self.Fibonacci_Recur(n - 2)
			self.memo[n] = f
			return f

# Great practice from MIT OCW and MITx 


def Charles():
	range = int(input("What is the order of the Fibonacci number you wish to find?\t"))
	if range < 0:
		print("Invalid, try again")
	elif (range > 1000):
		print("That would take too long to compute")
	elif (type(range) != type(int())):
		print("Please enter a number.")
	else:
		f = Fibonacci(range, {})
		print("Using the iterative approach\n")
		f.Fibonacci_Iter()
		print("Using the recursive memoisation approach")
		f.Fibonacci_Recur(range)
		for n in f.memo:
			print(f.memo[n])
			
Charles()
