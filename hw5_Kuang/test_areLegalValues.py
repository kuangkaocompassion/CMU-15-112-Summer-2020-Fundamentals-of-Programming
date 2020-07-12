def areLegalValues(values):
    
    numofSudoku = len(values)

    for num in range(1, numofSudoku+1):
        if values.count(num) > 1:
            return False

    return True

print(areLegalValues([1,0,0,4]))