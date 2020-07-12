#################################################
# hw1.py
#
# Your name:
# Your andrew id:
#################################################

import cs112_m20_week1_linter
import math

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

def getKthDigit(n, k):
    return 42

def colorBlender(rgb_v1, rgb_v2, midpoints, n):
    
    # when 'n' is out of range
    if n > (midpoints + 1) or n < 0:
        return None

    r_v1 = rgb_v1/1000000
    g_v1 = (rgb_v1%1000000)/1000
    b_v1 = (rgb_v1%1000000)%1000

    r_v2 = rgb_v2/1000000
    g_v2 = (rgb_v2%1000000)/1000
    b_v2 = (rgb_v2%1000000)%1000

    midpoints = float(midpoints+1) 
    rinterval = (r_v1 - r_v2) / midpoints 
    ginterval = (g_v1 - g_v2) / midpoints 
    binterval = (b_v1 - b_v2) / midpoints 
    rn = roundHalfUp (r_v1 - n*rinterval)
    gn = roundHalfUp (g_v1 - n*ginterval)
    bn = roundHalfUp (b_v1 - n*binterval)

    return rn*1000000+gn*1000+bn

#################################################
# Test Functions
#################################################

def testGetKthDigit():
    print('Testing getKthDigit()... ', end='')
    assert(getKthDigit(809, 0) == 9)
    assert(getKthDigit(809, 1) == 0)
    assert(getKthDigit(809, 2) == 8)
    assert(getKthDigit(809, 3) == 0)
    assert(getKthDigit(0, 100) == 0)
    assert(getKthDigit(-809, 0) == 9)
    print('Passed.')

def testColorBlender():
    print('Testing colorBlender()... ', end='')
    # http://meyerweb.com/eric/tools/color-blend/#DC143C:BDFCC9:3:rgbd
    assert(colorBlender(220020060, 189252201, 3, -1) == None)
    assert(colorBlender(220020060, 189252201, 3, 0) == 220020060)
    assert(colorBlender(220020060, 189252201, 3, 1) == 212078095)
    assert(colorBlender(220020060, 189252201, 3, 2) == 205136131)
    assert(colorBlender(220020060, 189252201, 3, 3) == 197194166)
    assert(colorBlender(220020060, 189252201, 3, 4) == 189252201)
    assert(colorBlender(220020060, 189252201, 3, 5) == None)
    # http://meyerweb.com/eric/tools/color-blend/#0100FF:FF0280:2:rgbd
    assert(colorBlender(1000255, 255002128, 2, -1) == None)
    assert(colorBlender(1000255, 255002128, 2, 0) == 1000255)
    assert(colorBlender(1000255, 255002128, 2, 1) == 86001213)
    assert(colorBlender(1000255, 255002128, 2, 2) == 170001170)
    assert(colorBlender(1000255, 255002128, 2, 3) == 255002128)
    print('Passed.')

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    # testGetKthDigit()
    testColorBlender()

def main():
    cs112_m20_week1_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
