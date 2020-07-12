#################################################
# hw2.py
#
# Your name:
# Your andrew id:
#################################################

import cs112_m20_day2_linter
import math

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def digitcount2 (n): 
    type (n) == int 
    return len(str(abs(n)))

#################################################
# Functions for you to write
#################################################


def digitcount (n):
    type (n) == int 
    count = 0
    while n > 0: 
        n //=  10
        count += 1
    return count


def digitcount2 (n): 
    type (n) == int 
    return len(str(abs(n)))

#print ("digit count Passed!")


def rotateNumber (n): 
    unitdigit = n%10 
    therest = n//10
    #print(unitdigit * 10 ** (digitcount2(n)-1) + therest)
    return unitdigit * 10 ** (digitcount2(n)-1) + therest

#print ("rotate number Passed!") 


def isPrime (n): 
    squareroot = int(n**(0.5))
    for index in range (2,squareroot+1):
            if n % index == 0:
                return False
            else: 
                continue
    return True

def isCircularPrime (n):
    length = len(str(n))
    newn   = n
    for i in range (length): 
        #print("nth rotation:", i)
        #print("current num:", newn)
        if isPrime(newn) == True: 
            #print("before rotate:", newn)
            newn = rotateNumber(newn)
            #print("after rotate:", newn)
        else: 
            return False
    return True              

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





   
#################################################
# Test Functions
################################################

def testRotateNumber():
    print('Testing rotateNumber()... ')
    assert(rotateNumber(1234) == 4123)
    assert(rotateNumber(4123) == 3412)
    assert(rotateNumber(3412) == 2341)
    assert(rotateNumber(2341) == 1234)
    assert(rotateNumber(5) == 5)
    assert(rotateNumber(111) == 111)
    print('Passed!')

def testIsCircularPrime():
    print('Testing isCircularPrime()... ')
    assert(isCircularPrime(2) == True)
    assert(isCircularPrime(11) == True)
    assert(isCircularPrime(13) == True)
    assert(isCircularPrime(79) == True)
    assert(isCircularPrime(197) == True)
    assert(isCircularPrime(1193) == True)
    assert(isCircularPrime(42) == False)
    print('Passed!')

def testNthCircularPrime():
    print('Testing nthCircularPrime()... ')
    assert(nthCircularPrime(0) == 2)
    assert(nthCircularPrime(4) == 11)
    assert(nthCircularPrime(5) == 13)
    assert(nthCircularPrime(11) == 79)
    assert(nthCircularPrime(15) == 197)
    assert(nthCircularPrime(25) == 1193)
    print('Passed!')

def testPlay112():
    print("Testing play112()... ", end="")
    assert(play112( 5 ) == "88888: Unfinished!")
    assert(play112( 521 ) == "81888: Unfinished!")
    assert(play112( 52112 ) == "21888: Unfinished!")
    assert(play112( 5211231 ) == "21188: Unfinished!")
    assert(play112( 521123142 ) == "21128: Player 2 wins!")
    assert(play112( 521123151 ) == "21181: Unfinished!")
    assert(play112( 52112315142 ) == "21121: Player 1 wins!")
    assert(play112( 523 ) == "88888: Player 1: move must be 1 or 2!")
    assert(play112( 51223 ) == "28888: Player 2: move must be 1 or 2!")
    assert(play112( 51211 ) == "28888: Player 2: occupied!")
    assert(play112( 5122221 ) == "22888: Player 1: occupied!")
    assert(play112( 51261 ) == "28888: Player 2: offboard!")
    assert(play112( 51122324152 ) == "12212: Tie!")
    print("Passed!")

#################################################
# Main
################################################

def testAll():
    # comment out the tests you do not wish to run!
    testRotateNumber()
    testIsCircularPrime()
    testNthCircularPrime()
    #testPlay112()

def main():
    cs112_m20_day2_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
