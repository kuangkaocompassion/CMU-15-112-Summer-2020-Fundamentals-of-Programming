#################################################
# hw3.py
#
# Your name:
# Your andrew id:
#################################################

import cs112_m20_day3_linter
import string, random

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

def patternedMessage(msg, pattern):
	newmessage = msg.replace(" ","") 
	pattern = pattern.strip("\n")
	result = ""
	index = -1
	length = len(newmessage)
	for i in pattern:
			if i in string.punctuation or i in string.ascii_letters == True: 
				index += 1
				new = newmessage[index % length]
				result += new 
			if i.isspace() == True:
				result += i
	return result

def getEvalSteps(expr):
		return 42

#################################################
# Test Functions
#################################################

def testPatternedMessage():
		print("Testing patternedMessage()...", end="")
		parms = [
		("Go Pirates!!!", """
***************
******   ******
***************
"""),
		("Three Diamonds!","""
		*     *     *
	 ***   ***   ***
	***** ***** *****
	 ***   ***   ***
		*     *     *
"""), 
		("Go Steelers!","""
													oooo$$$$$$$$$$$$oooo
											oo$$$$$$$$$$$$$$$$$$$$$$$$o
									 oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
	 o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ '$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
'$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
	$$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
	$$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  '$$$
	 '$$$'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$
		$$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$o
	 o$$'   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
	 $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$' '$$$$$$ooooo$$$$o
	o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
	$$$$$$$$'$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$'
 ''''       $$$$    '$$$$$$$$$$$$$$$$$$$$$$$$$$$$'      o$$$
						'$$$o     '$$$$$$$$$$$$$$$$$$'$$'         $$$
							$$$o          '$$'$$$$$$'           o$$$
							 $$$$o                                o$$$'
								'$$$$o      o$$$$$$o'$$$$o        o$$$$
									'$$$$$oo     '$$$$o$$$$$o   o$$$$'
										 '$$$$$oooo  '$$$o$$$$$$$$$'
												'$$$$$$$oo $$$$$$$$$$
																'$$$$$$$$$$$
																		$$$$$$$$$$$$
																		 $$$$$$$$$$'
																			'$$$'
"""),
("A-C D?", """
*** *** ***
** ** ** **
"""),
		("A", "x y z"),
		("The pattern is empty!", "")
		]
		solns = [
"""
GoPirates!!!GoP
irates   !!!GoP
irates!!!GoPira
"""
,
"""
		T     h     r
	 eeD   iam   ond
	s!Thr eeDia monds
	 !Th   ree   Dia
		m     o     n
"""
,
"""
													GoSteelers!GoSteeler
											s!GoSteelers!GoSteelers!GoS
									 teelers!GoSteelers!GoSteelers!GoS         te   el er
	 s ! Go        Steelers!GoSteelers!GoSteelers!GoSteel       er s! GoSt
ee l e rs      !GoSteeler    s!GoSteelers!    GoSteelers       !GoSteel
ers!GoSte     elers!GoSt      eelers!GoSt      eelers!GoSt    eelers!G
	oSteele    rs!GoSteele      rs!GoSteele      rs!GoSteelers!GoSteeler
	s!GoSteelers!GoSteelers    !GoSteelers!G    oSteelers!GoSt  eele
	 rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSteel     ers!
		GoS   teelers!GoSteelers!GoSteelers!GoSteelers!GoSteelers     !GoSt
	 eele   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSt       eele
	 rs!    GoSteelers!GoSteelers!GoSteelers!GoSteelers!Go Steelers!GoSteele
	rs!GoSteelers  !GoSteelers!GoSteelers!GoSteelers!GoS   teelers!GoSteelers
	!GoSteelers!G   oSteelers!GoSteelers!GoSteelers!Go     Steel
 ers!       GoSt    eelers!GoSteelers!GoSteelers!G      oSte
						elers     !GoSteelers!GoSteelers!         GoS
							teel          ers!GoSteel           ers!
							 GoSte                                elers
								!GoSte      elers!GoSteele        rs!Go
									Steelers     !GoSteelers!   GoStee
										 lers!GoSte  elers!GoSteeler
												s!GoSteele rs!GoSteel
																ers!GoSteele
																		rs!GoSteeler
																		 s!GoSteeler
																			s!GoS
""",
"""
A-C D?A -CD
?A -C D? A-
""",
"A A A",
""

		]
		for i in range(len(parms)):
				msg,pattern = parms[i]
				soln = solns[i]
				soln = soln.strip("\n")
				observed = patternedMessage(msg, pattern)
				print ("\nsol: \n",soln, "\n", "+"*10, "\n", \
					"\nobserved: \n", observed, "\n", "-"*10, "\n")
				assert(observed == soln)
		print("Passed!")

def testGetEvalSteps():
		print("Testing getEvalSteps()...", end="")
		assert(getEvalSteps("0") == "0 = 0")
		assert(getEvalSteps("2") == "2 = 2")
		assert(getEvalSteps("3+2") == "3+2 = 5")
		assert(getEvalSteps("3-2") == "3-2 = 1")
		assert(getEvalSteps("3**2") == "3**2 = 9")
		assert(getEvalSteps("31%16") == "31%16 = 15")
		assert(getEvalSteps("31*16") == "31*16 = 496")
		assert(getEvalSteps("32//16") == "32//16 = 2")
		assert(getEvalSteps("2+3*4") == "2+3*4 = 2+12\n      = 14")
		assert(getEvalSteps("2*3+4") == "2*3+4 = 6+4\n      = 10")
		assert(getEvalSteps("2+3*4-8**3%3") == """\
2+3*4-8**3%3 = 2+3*4-512%3
						 = 2+12-512%3
						 = 2+12-2
						 = 14-2
						 = 12""")
		assert(getEvalSteps("2+3**4%2**4+15//3-8") == """\
2+3**4%2**4+15//3-8 = 2+81%2**4+15//3-8
										= 2+81%16+15//3-8
										= 2+1+15//3-8
										= 2+1+5-8
										= 3+5-8
										= 8-8
										= 0""")
		print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
		testPatternedMessage()
		testGetEvalSteps()

def main():
		cs112_m20_day3_linter.lint()
		testAll()

if __name__ == '__main__':
		main()
