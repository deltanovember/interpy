import math
def poly(n, s):
	return 0.25*n*s*s/math.tanh(math.pi/n)
print(poly(7,3))