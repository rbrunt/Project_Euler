def fibonacci(n):
	"""A generator that returns numbers in a fibonacci sequence"""
	# Set up initial values:
	current = 1
	next = 2
	# Now we calculte n fibonacci numbers, yeilding each one in turn:
	for i in xrange(n):
		yield current
		current, next = next, current + next

def finalFibonacci(n):
	return list(fibonacci(n))[-1]

def findNotExceeding(theMax):
	n = 1
	while finalFibonacci(n) < theMax:
		n += 1
	
	return n-1, finalFibonacci(n-1)

if __name__ == "__main__":
	print "Finding the last fibonacci term under 4 000 000..."
	n, value = findNotExceeding(4000000)
	print "The term is:", n
	print "Which has a final value of:", value
	terms = list(fibonacci(n))
	print "The terms are:", terms
	print "reduce list so only even terms remain:"
	evenTerms = [x for x in terms if x % 2 == 0]
	print "even terms:", evenTerms
	print "the sum of these terms is simply:"
	total = sum(evenTerms)
	print total