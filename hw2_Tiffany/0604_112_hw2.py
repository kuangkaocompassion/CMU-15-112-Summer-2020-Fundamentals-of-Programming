

def digitcount (n):
	type (n) == int 
	count = 0
	while n > 0: 
		n //=  10
		count += 1
	return count

assert (digitcount(1234)== 4)

def digitcount2 (n): 
	type (n) == int 
	return len(str(abs(n)))

assert (digitcount2 (1234)==4) 
#print ("digit count Passed!")


def rotatenumber (n): 
	unitdigit = n%10 
	therest = n//10
	#print(unitdigit * 10 ** (digitcount2(n)-1) + therest)
	return unitdigit * 10 ** (digitcount2(n)-1) + therest
	
assert (rotatenumber (1234) == 4123) 
#print ("rotate number Passed!") 


def isPrime (n): 
	squareroot = int(n**(0.5))
	for index in range (2,squareroot+1):
			if n % index == 0:
				return False
			else: 
				continue
	return True
#print (isPrime(4))

def isCircularPrime (n):
	length = len(str(n))
	newn   = n
	for i in range (length): 
		if isPrime(newn) == True: 
			newn = rotatenumber(n) 
			continue
		else: 
			return False
	return True 			


#print (isCircularPrime(1193))

def nthCircularPrime (n): 
    testNum = 2
    count = -1 
    #listisCircularPrime = [] 
    while count <  n: 
        if isCircularPrime(testNum) == True: 
            count += 1
            #listisCircularPrime.append(testNum)
            #print ("Number of count:",count)
            #print ("TestNum:", testNum)
            #print("="*10)
            testNum += 1
        else: 
            #print("continues' number:", testNum)
            #print("#"*10)
            testNum += 1
            continue 
    #print(listisCircularPrime) 
    return testNum-1

#print(isCircularPrime(10))
#print (nthCircularPrime(5))
if nthCircularPrime(4) == 11:
	print("Yes")
else:
	print("No")
'''
def nthCircularPrime (number, n):
	if isCircularPrime (number) == "is a prime number": 
		if n == 1: 
			return number
		if n == 2: 
			n1 = rotatenumber (number)
			return n1 
		if n == 3: 
			n2 = rotatenumber (n2) 
			return n2
		if n == 4: 
			n3 = rotatenumber (n3)
		 	return n3

print (nthCircularPrime(1193,2))



 


import string
print(string.ascii_lowercase) 

numlist = []
for n in range (11): 
	numlist.append(n) 

print numlist

print (numlist[::-1])

for n in range (len(s)): 
	print (n, s[n])

for rows in range (5):
	for cols in range (0, rows -1): 
		print ("*.  ") 

dogs = 42
cats = 3
print("%s %s" % ("dogs", "cats"))
print("%d %d" % (dogs, cats))

#1 
numlist1 = [9,8,3,4,2,21,23,10]
target = 27 
seen= {}
for n in range (7): 
	num2 = target - numlist1[n]
	if num2 in seen:
		print (seen(num2),n)

#2 
list_1 = [9, 8, 3, 4, 2, 21, 23, 10] 
list_2 = [3, 5, 10, 100]

joinlist= list_1 + list_2 
joinlist.sort ()

print (joinlist)

#3
sentence = "a set of words that is complete in itself" 
wordlist = sentence.split()
print(len(wordlist [-1])) 

sentence2 = "Comprehensive up-to-date news coverage"
wordlist2 = sentence2.split()
print(len(wordlist2[-1])) 

'''
























