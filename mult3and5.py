

#Find the sum of all the multiples of 3 or 5 less than 1000.

#Brute force method - lots ofo
def addMultiple(integer, lessThan):
	factor = 1;
	multiple = total = 0;
	while(multiple<lessThan):
		total = total + (factor*integer)

		factor = factor + 1
		multiple = factor * integer

	return total

print "BF sum of 3s"
print  addMultiple(3, 1000)
print "BF sum of 5s"
print  addMultiple(5, 1000)
print "BF sum of 15s"
print  addMultiple(15, 1000)

result = addMultiple(3, 1000) + addMultiple(5, 1000) - addMultiple(15, 1000)
print "Brute Force"
print result

#####
print "**************************"

def addMultiplePairs(integer, lessThan):
	maxInt = lessThan-1
	maxMult = maxInt - maxInt%integer
	maxFactor = maxMult/integer

	if(maxFactor%2):
		middle = (maxMult + integer)/2
		sumOfPairs = (maxFactor-1)/2 * (maxMult+integer)
	else:
		middle = 0
		sumOfPairs = maxFactor/2 * (maxMult+integer)

	total = middle + sumOfPairs
	return total

print "SP sum of 3s"
print  addMultiplePairs(3, 1000)
print "SP sum of 5s"
print  addMultiplePairs(5, 1000)
print "SP sum of 15s"
print  addMultiplePairs(15, 1000)

result = addMultiplePairs(3, 1000) + addMultiplePairs(5, 1000) - addMultiplePairs(15, 1000)
print "Summing pairs"
print result