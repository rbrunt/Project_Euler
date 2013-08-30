def checkPythagoreanTriplet(a, b, c):
	if not a < b < c:
		print a, b, c
		raise Exception

	if a**2 + b**2 == c**2:
		return True
	else:
		return False

if __name__ == "__main__":
	#dostuff

	for a in xrange(1,1001):
		for b in xrange(a + 1, (1001 - a) / 2):
			c = 1000 - a - b
			if checkPythagoreanTriplet(a, b, c):
				print a, b, c
				print "product: ", a*b*c

	print "done"