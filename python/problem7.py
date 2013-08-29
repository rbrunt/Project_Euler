from problem3 import checkPrime
from time import time

def findNthPrime(nth):
	n = 0
	current = 2
	while n < nth:
		n +=1
		while True:
			if checkPrime(current):
				current += 1
				break
			else:
				current += 1
	return current - 1

def listPrimesToNth(nth):
	n = 0
	current = 2
	primes = []
	while n < nth:
		n +=1
		while True:
			if checkPrime(current):
				primes.append(current)
				current += 1
				break
			else:
				current += 1
	return primes

if __name__ == "__main__":
	#find 10001st prime:
	starttime = time()

	current = findNthPrime(10001)

	endtime = time()
	print "answer is", current - 1
	print "took", (endtime - starttime), "seconds"