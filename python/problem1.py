from time import time

def calculatesum(x):
	ans = 0
	for i in range(x):
		if (i%3==0 or i%5==0):
			ans += i
		i+=1
	return ans

start = time()
print "answer:", calculatesum(1000)
print "time taken =", time() - start, "seconds"