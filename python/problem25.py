import math
from problem2 import *

def findFirstDigits(digits):
	n = 1
	while int(math.log10(finalFibonacci(n)))+1 < digits: # simple way of finding number of digits without converting to string
		n += 1
	return n

if __name__ == "__main__":
	print "First term of the fibonacci sequence to be 1000 characters or more long:", findFirstDigits(1000)