#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143?

#Brute force. This solution takes WAY too long to run. INVALID ANSWER
def primeFactor(integer):
	n = integer-1
	factor = 0

	while(n>1):
		if(integer%n==0):
			if(isPrime(n)):
				factor = n
				break
			else:
				continue
		n = n-1

	return factor

def isPrime(factor):
	i=2
	while(True):
		if(i==factor):
			return True
		if(factor%i==0):
			return False
		i = i+1


#result = primeFactor(600851475143)
#print result

#Next iteration.  Divide and conquer!
def primeFactorTwo(integer):
	factor = 0
	n = 2

	while(n<=integer):
		while(integer%n==0):
			integer=integer/n
			factor = n
		n=n+1

	return factor

print primeFactorTwo(600851475143)