def sumSquares(n):
	total = 0
	for i in xrange(1,n+1):
		total += i**2
	return total

def squareSum(n):
	total = sum(xrange(1,n+1))
	return total**2

if __name__ == "__main__":

	maximum = 100

	sumsquares = sumSquares(maximum)
	squaresum = squareSum(maximum)

	print "natural numbers up to %i" % maximum
	print "sumsquares:", sumsquares
	print "squareSum:", squaresum
	print "differnce:", abs(squaresum - sumsquares)