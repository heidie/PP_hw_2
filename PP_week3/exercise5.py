def getNumOfE(word):
	numOfE = 0

	for char in word:
		if char == 'e':
			numOfE++
	return numOfE

print getNumOfE('next people')



