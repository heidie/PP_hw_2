def seperateWord(inputWord):
	seperateList = list(inputWord)
	return seperateList

def getInverse(seperateList):
	seperateList.reverse()
	inverseWord = ''.join(seperateList)
	return inverseWord


inputWord = raw_input('input a word: ')
seperateList = seperateWord(inputWord)
inverseWord = getInverse(seperateList)
print inverseWord
