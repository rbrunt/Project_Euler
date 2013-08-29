from math import sqrt

def checkPrime(number):
	isPrime = True
	for i in xrange(1,int(sqrt(number))+1):
		if i != 1 and i != number:
			if number % i == 0:
				isPrime = False
				break

	return isPrime

def factors(n):
	return set(reduce(list.__add__, ([i, n//i] for i in xrange(1, int(sqrt(n)) + 1) if n % i == 0)))

def primeFactors(n):
	factors = factors(n)
	primefactors = []
	for factor in factors:
		if checkPrime(factor):
			primefactors.append(factor)
	return primefactors


if __name__ == "__main__":
	n = 600851475143

	factors = factors(n)
	primefactors = []
	print n, "has the factors: ", factors

	for factor in factors:
		if checkPrime(factor):
			primefactors.append(factor)


	print "of these, the following a prime: ", primefactors

	print "the largest of these prime factors is:", max(primefactors)