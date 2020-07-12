'''
#2 
def areAmicableNumbers (x,y):
	xlist = []
	ylist = []
	for n in range (1,x):
		if x % n == 0:
			xlist.append(n)
	if sum(xlist) == y:
		for n in range (1,y):
			if y%n == 0:
				ylist.append(n)
	else:
		return False

	if sum(ylist) == x: 
		return True
	else: 
		return False


print (areAmicableNumbers(2620,2924))

def splitNumber (n,i): 
	x = n//10**i 
	y = n%10**i 
	return (x,y)

#3
def nthMarriedNumber (n): 
	marriedlist []
	x = sum(marriedlist)
	first = 11 
	while x < n: 
		for i in range (digicount(first)): 
			splitNumber(first, i) 
			if areAmicableNumbers (x,y) == True:
				marriedlist.append(x)
	return marriedlist.index(n)



def digicount(n): 
	num = 0 
	while n > 0: 
		n//10
		num+=1 
	return num 

print (digicount(234))

#4 
def runStringProgram (s): 
	splitstring = s.split(':')
	a = splitstring [0]
	b = splitstring [1]
	c = b.split('.')
	lenofc = len(c)
	print (a,b,c)
	for i in range (lenofc): 
		if "S" in c[i]: 
			Num = c[i].strip("S")
			if digicount(Num) == 1: 
				a = a[:Num] 
			if digicount(Num) == 2:
				one = Num[0]
				two = Num [1]
				a = a[one:two]
		if "L" in c[i]:
			if a.islower() == True:
				return True
		return False 

print (runStringProgram("aaaBBBccc:S6.L?.S13.L?"))
''' 

def runStringProgram (s) :
	#s = "aaaBBBccc:S6.L?.S13.L?"
	lengthofs = len(s) 

	colon = s.index(":")
	print(colon)

	data = s[:colon]
	c = s[colon+1:]
	lengthofc= len(c)
	#find all .
	for n in range (lengthofc):
		if c[n] == "S":
			if c[n+2] == ".":
				num = int(c[n+1] )
				print("num", num)
				tdata = data[:num] 
				print("data:", tdata)
				if tdata.islower() == True:
					return print("ya", True)
			else: 
				f = int(c[n+1])
				se = int(c[n+2])
				print("fse:", f, se)
				ttdata= data[f:se]
				print("data2:", ttdata)
				if ttdata.islower() == True:
					return True
	return False
print (runStringProgram("qqGGaaab:S35.L?.S26.L?.S17.L?"))




		






