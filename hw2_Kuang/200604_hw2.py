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


def rotateNumber (n): 
    unitdigit = n%10 
    therest = n//10
    return unitdigit * 10 ** (digitcount2(n)-1) + therest
    
def isPrime(num):
# Program to check if a number is prime or not

# To take input from the user
#num = int(input("Enter a number: "))

    # prime numbers are greater than 1
    if num > 1:
       # check for factors
       for i in range(2,num):
           if (num % i) == 0:
               #print(num,"is not a prime number")
               #print(i,"times",num//i,"is",num)
               break
       else:
           return True
           
    # if input number is less than
    # or equal to 1, it is not prime
    else:
       return False

def isCircularPrime(x):
    testNum = x
    for length in range(len(str(x))):
        if not isPrime(testNum):
            return False
        testNum = rotateNumber(testNum)
    return True

def nthCircularPrime(n):
    ans = 2
    count = 0 
    # 
    while count < n:
        ans += 1
        if isCircularPrime(ans):
            #listCircularPrime.append(ans)
            count += 1
    return ans
    
#print(nthCircularPrime(11)[1])
#print(isCircularPrime(20))

def play112(game):
    return 42

#################################################
# Test Functions
################################################

def testRotateNumber():
    print('Testing rotateNumber()... ', end='')
    assert(rotateNumber(1234) == 4123)
    assert(rotateNumber(4123) == 3412)
    assert(rotateNumber(3412) == 2341)
    assert(rotateNumber(2341) == 1234)
    assert(rotateNumber(5) == 5)
    assert(rotateNumber(111) == 111)
    print('Passed!')

def testIsCircularPrime():
    print('Testing isCircularPrime()... ', end='')
    assert(isCircularPrime(2) == True)
    assert(isCircularPrime(11) == True)
    assert(isCircularPrime(13) == True)
    assert(isCircularPrime(79) == True)
    assert(isCircularPrime(197) == True)
    assert(isCircularPrime(1193) == True)
    assert(isCircularPrime(42) == False)
    print('Passed!')

def testNthCircularPrime():
    print('Testing nthCircularPrime()... ', end='')
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
    testPlay112()

def main():
    cs112_m20_day2_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
