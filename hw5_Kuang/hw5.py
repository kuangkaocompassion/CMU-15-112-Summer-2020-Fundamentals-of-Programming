#################################################
# hw5.py
#
# Your name:
# Your andrew id:
#################################################

import cs112_m20_unit5_linter
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
# Sudoku Functions
#################################################

def areLegalValues(values):
    
    numofSudoku = len(values)

    for num in range(1, numofSudoku+1):
        if values.count[idx] > 1:
            return False

    return True

def isLegalRow(board,row):
    return 42

def isLegalCol(board,col):
    return 42

def isLegalBlock(board,block):
    return 42

def isLegalSudoku(board):
    return 42




#################################################
# Chess Functions
#################################################


def getValidRookMoves(board, startRow, startCol):
    return 42

def getValidBishopMoves(board, startRow, startCol):
    return 42

def getValidQueenMoves(board, startRow, startCol):
    return 42

def getValidKnightMoves(board, startRow, startCol):
    return 42

def getValidPawnMoves(board, startRow, startCol):
    return 42

def getValidKingMoves(board, startRow, startCol):
    return 42

def getValidChessMoves(board, startRow, startCol):
    return 42

#################################################
# Test Functions
#################################################

def testIsLegalSudoku():
    print("Testing isLegalSudoku...")
    # Your tests here! Remember to write test functions for helpers as well
    assert(42 == 42)
    print("Passed!")

def testGetValidChessMoves():
    print("Testing getValidChessMoves...")
    # Your tests here! Remember to write test functions for helpers as well
    assert(42 == 42)
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testIsLegalSudoku()
    testGetValidChessMoves()

def main():
    cs112_m20_unit5_linter.lint()
    testAll()

if __name__ == "__main__":
    main()
