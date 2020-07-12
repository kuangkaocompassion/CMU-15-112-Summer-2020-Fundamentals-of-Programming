def patternedMessage(msg, pattern):
    #pattern = pattern.strip()

    #print(pattern, len(pattern))
    
    nonSpaceCount  = 0
    numIdxMsg = 0
    msgList = []
    ansStr  = ""

    # Get all chars out into the list
    for charMsg in msg:
      if charMsg != " ":
        msgList.append(charMsg)

    # Create ansStr
    for charPattern in pattern:
      if charPattern == "*":
        #print("charPattern for replacing:", charPattern)
        numIdxMsg      = nonSpaceCount%len(msgList)
        ansStr        += msgList[numIdxMsg]
        nonSpaceCount += 1
      else:
        ansStr += charPattern

    return ansStr

print(patternedMessage("Go Pirates!!!", """
***************
******   ******
***************
"""))
print(patternedMessage("Three Diamonds!","""
    *     *     *
   ***   ***   ***
  ***** ***** *****
   ***   ***   ***
    *     *     *
"""))