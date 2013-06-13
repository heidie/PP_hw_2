def seperateWord(inputWord):
	seperateList = list(inputWord)
	return seperateList

def getInverse(seperateList):
	seperateList.reverse()
	inverseWord = ''.join(seperateList)
	return inverseWord

def checkInverse(word, inverseWord):
    if(word is inverseWord):
        return true
    else:
        return false

inputWord = raw_input('input a word: ')
seperateList = seperateWord(inputWord)
inverseWord = getInverse(seperateList)
print inverseWord

print checkInverse(inputWord, inverseWord)