from time import time

def  checkPalindrome(number):
	string = str(number)
	if string == string[::-1]:
		return True
	else:
		return False



if __name__ == "__main__":
	start = time()

	palindromes = set()

	for i in xrange(100,1000):
		for j in xrange(499,1000):
			if checkPalindrome(i*j):
				palindromes.add(i*j)

	answer = max(palindromes)
	totalTime = time() - start

	print "palindromes:", palindromes
	print "largest one is:", max(palindromes)
	print "took", totalTime, "seconds"