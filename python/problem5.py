from problem3 import factors, primeFactors
from time import time

def bruteForce(maximum):
	n = 1
	while not range(1,maximum+1) == sorted(factors(n))[0:maximum]:
		n += 1
	return n


def highestCommonFactor(a, b):
	# Highest common factor is the multiple of a and b's common prime factors.
	# Can find by euclid's algorithm: hcf(a,0) = a ; hcf(a,b) = hcf(b,a%b)
	while b != 0:
		a, b = b, a % b
	return a

def  lowestCommonMultiple(a, b):
	return a*b/highestCommonFactor(a, b)

def findAnswer(maximum):
	return reduce(lowestCommonMultiple, range(1, maximum+1))

if __name__ == "__main__":
	startTime = time()

	maximum = 20
	answer = findAnswer(maximum) # Takes about 0.003s
	#answer = findAnswer(100000) # Takes ~ 26 seconds on an i7 laptop @ 1.6 GHz - pretty efficient!

	print "Smallest number with the numbers 1-%i is" % maximum, answer
	print "Took", time() - startTime, "seconds"
