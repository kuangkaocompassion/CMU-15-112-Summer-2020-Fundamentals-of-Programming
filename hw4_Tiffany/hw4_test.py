import string

dictionary2   = ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
letterScores2 = [1+(i%5) for i in range(26)]
hand2         = ["x", "y", "z"]

def bestScrabbleScore(dictionary, letterScores, hand):
    #hand = ['a','c','e'] 
    
    #make alphabet list
    alphabet_string = string.ascii_lowercase
    alphabet_list = list (alphabet_string)
    tuplelist = [] # store (word, score)
    maxScore  = 0

    lengthofdict = len(dictionary) 
    for n in range (lengthofdict): 
        x = list(dictionary[n]) #finds the first word and put in list
        lenofx = len(x)
        for m in range (lenofx): 
            verifiedword = []
            if x[m] in hand:
                verifiedword.append (x[m])
            else:
                verifiedword = []
                n += 1 #?
                break 
        if verifiedword != []: 
            indexlist = [] #all numbers?
            lengthofverifiedword = len(verifiedword)
            for y in range (lengthofverifiedword):
                indexofal = alphabet_list.index(verifiedword[y])
                indexlist.append(indexofal) #?

            lengthofindexal = len(indexlist)
            scoreslist = []
            for z in range (lengthofindexal):
                scores = letterScores[indexlist[z]]
                scoreslist.append (scores)
                sumofscores = sum(scoreslist)
                tuplelist.append((verifiedword,sumofscores))
    return tuplelist

print(bestScrabbleScore(dictionary2, letterScores2, hand2))

