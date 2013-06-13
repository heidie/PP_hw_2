def getValue(num):
	if(num > 0 and num <10):
		return num+10
	elif(num > 10 and num < 100):
		return num*0.1
	else:
		return False

print getValue(5)
print getValue(24)
print getValue(-10)


