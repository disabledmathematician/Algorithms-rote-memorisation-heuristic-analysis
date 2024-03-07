def somehow_derivative(f, a, h=0.000000001):
	return ((f(a + h) - f(a - h)) / (2 * h))

def CharlesDoingNewtonsMethod(f, x, maxiter=100):
	g = x
	while abs(round(g ** 2, 7)) != abs(round(x, 7)):
		g -= (f(g) - x) / somehow_derivative(f, g, 0.0001)
		print("{}".format(g))
	print("The numerical approximation evaluated at the point is: {}".format(g))
	print("f of g is {} hence the square root is {}".format(f(g), g))
	
CharlesDoingNewtonsMethod(lambda x: x ** 2, 2, 100)

# Thanks forever MIT and Python Software Foundation and edX.org and Harvard staff and National Cryptologic Museum. Really thankful that I accomplished so many wonderful things as a badly disabled person who was all poor and dying from a brain tumour

# Charles Truscott Watters