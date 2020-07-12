dictionary2   = ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
letterScores2 = [1+(i%5) for i in range(26)]
hand2        = list("wxz")

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

print(bestScrabbleScore(dictionary2, letterScores2, hand2))



