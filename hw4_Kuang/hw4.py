#################################################
# hw4.py
#
# Your name:
# Your andrew id:
#################################################

import cs112_m20_day5_linter
import copy

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
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

def nondestructiveRotateList(L, n):
    return 42

def destructiveRotateList(L, n):
    return 42

def bestScrabbleScore(dictionary, letterScores, hand):
    
    tupleScoreWordPair = []
    tupleletterScores  = []
    ans                = []
    maxScore           = 0

    # key:value = letter:score
    for idx in range(26):
        tupleletterScores.append((str.lower(chr(65+idx)), letterScores[idx]))

    for wordOption in dictionary:
        highScore              = 0
        # make a copy of hand, able to del and add
        temphand               = list.copy(hand)  
        # make the word into list, able to del and add
        listWordOption         = list(wordOption) 
        lengthoflistWordOption = len(listWordOption)

        for char in listWordOption:
            if char in temphand:
                temphand.remove(char)
                lengthoflistWordOption -= 1
                
                # find the score of the char, and add score to highscore
                for letterScorePair in tupleletterScores:
                    if letterScorePair[0] == char:
                        highScore += letterScorePair[1]


        # wordOption can be created
        if lengthoflistWordOption == 0:
            tupleScoreWordPair.append((wordOption,highScore))
        else:
            highScore = 0
        
        # update maximum score
        if highScore > maxScore:
            maxScore = highScore

    for pair in tupleScoreWordPair:
        if pair[1] == maxScore:
            ans.append(pair[0])
    
    if len(ans) == 1:
        return (ans[0], maxScore)

    if maxScore == 0:
        return None

    return (ans, maxScore)

def runSimpleProgram(program, args):
    return 42

#################################################
# Test Functions
#################################################

def isNondestructive(f,L,a): # Checks to make sure f(L,a) does not modify L
    unmodifiedCopy = copy.deepcopy(L)
    b = f(L,a)
    return L == unmodifiedCopy

def testNondestructiveRotateList():
    print("Testing nondestructiveRotateList()...", end="")
    assert(nondestructiveRotateList([], 42) == [])
    assert(nondestructiveRotateList([1,2,3,4], -1) == [2,3,4,1])
    assert(nondestructiveRotateList([1,2,3,4], 0) == [1,2,3,4])
    assert(nondestructiveRotateList([1,2,3,4], 1) == [4,1,2,3])
    assert(nondestructiveRotateList([1,2,3,4], 2) == [3,4,1,2])
    assert(nondestructiveRotateList([1,2,3,4], 3) == [2,3,4,1])
    assert(nondestructiveRotateList([1,2,3,4], 5) == [4,1,2,3])
    isNondestructive(nondestructiveRotateList,[1,2,3,4],1)
    isNondestructive(nondestructiveRotateList,[1,2,3,4],2)
    isNondestructive(nondestructiveRotateList,[1,2,3,4],3)
    print("Passed!")

def testDestructiveRotateList():
    print("Testing destructiveRotateList()...", end="")
    L = [1,2,3,4]
    assert(destructiveRotateList(L,1) == None)
    assert(L == [4,1,2,3])
    assert(destructiveRotateList(L,2) == None)
    assert(L == [2,3,4,1])
    assert(destructiveRotateList(L,7) == None)
    assert(L == [3,4,1,2])

# there are lots of test cases here :)
def testBestScrabbleScore():
    print("Testing bestScrabbleScore()...", end="")
    def dictionary1(): return ["a", "b", "c"]
    def letterScores1(): return [1] * 26
    def dictionary2(): return ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
    def letterScores2(): return [1+(i%5) for i in range(26)]
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("ace")) ==
            (["a", "c"], 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
            ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("z")) == None)
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyz")) ==
            (["xyz", "zxy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyzy")) ==
            (["xyz", "zxy", "yy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyq")) ==
            ("yx", 9))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("yzz")) ==
            ("zzy", 7))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("wxz")) ==
            None)
    print("Passed!")

def testRunSimpleProgram():
    print("Testing runSimpleProgram()...", end="")
    largest = """! largest: Returns max(A0, A1)
                   L0 - A0 A1
                   JMP+ L0 a0
                   RTN A1
                   a0:
                   RTN A0"""
    assert(runSimpleProgram(largest, [5, 6]) ==  6)
    assert(runSimpleProgram(largest, [6, 5]) == 6)
    assert(runSimpleProgram(largest, [6, 6]) == 6)
    assert(runSimpleProgram(largest, [42, -16]) == 42)
    sumToN = """! SumToN: Returns 1 + ... + A0
                ! L0 is a counter, L1 is the result
                L0 0
                L1 0
                loop:
                L2 - L0 A0
                JMP0 L2 done
                L0 + L0 1
                L1 + L1 L0
                JMP loop
                done:
                RTN L1"""
    multiply = """! multiply: A0 * A1
                L0 0
                L1 0
                loop:
                L2 - L0 A0
                JMP0 L2 done
                L0 + L0 1
                L1 + L1 A1
                JMP loop
                done:
                RTN L1"""
    assert(runSimpleProgram(sumToN, [0]) ==  0)
    assert(runSimpleProgram(sumToN, [3]) ==  1+2+3)
    assert(runSimpleProgram(sumToN, [5]) ==  1+2+3+4+5)
    assert(runSimpleProgram(multiply, [5,5]) == 5*5)
    assert(runSimpleProgram(multiply, [6,7]) == 6*7)
    assert(runSimpleProgram(multiply, [10,15]) == 10*15)
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    #testNondestructiveRotateList()
    #testDestructiveRotateList()
    testBestScrabbleScore()
    #testRunSimpleProgram()

def main():
    cs112_m20_day5_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
