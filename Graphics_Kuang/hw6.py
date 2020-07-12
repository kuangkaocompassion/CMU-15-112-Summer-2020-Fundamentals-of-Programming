#################################################
# hw6.py
#
# Your name:
# Your andrew id:
#################################################

import cs112_m20_unit6_linter
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

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

import basic_graphics

def drawLittleGrid(canvas, upperPoint, lowerPoint, dimension, board):
    
    width_of_little_gap  = (lowerPoint[0]-upperPoint[0])/dimension
    height_of_little_gap = (lowerPoint[1]-upperPoint[1])/dimension

    for num_of_rows in range(dimension):
        upper_point_little_grid_1 = (upperPoint[0], 
                                     upperPoint[1]+
                                     num_of_rows*width_of_little_gap)
        lower_point_little_grid_1 = (upperPoint[0]+width_of_little_gap
                               , (upperPoint[1]+height_of_little_gap)+
                               num_of_rows*width_of_little_gap)
        canvas.create_rectangle(upper_point_little_grid_1[0],
                                upper_point_little_grid_1[1],
                                lower_point_little_grid_1[0],
                                lower_point_little_grid_1[1])

        textLocation_x = ((upper_point_little_grid_1[0]+
                           lower_point_little_grid_1[0])/2)
        textLocation_y = ((upper_point_little_grid_1[1]+
                           lower_point_little_grid_1[1])/2)           

        textInt = board[num_of_rows][0]

        canvas.create_text(textLocation_x, textLocation_y, text=textInt,
                       fill="purple", font="Helvetica 10 bold underline")
        
        for num_of_columns in range(dimension):
            canvas.create_rectangle(upper_point_little_grid_1[0]+
                                    num_of_columns*height_of_little_gap,
                                    upper_point_little_grid_1[1],
                                    lower_point_little_grid_1[0]+
                                    num_of_columns*height_of_little_gap,
                                    lower_point_little_grid_1[1])
            
            textLocation_x = ((upper_point_little_grid_1[0]+
                             num_of_columns*height_of_little_gap)+
                              (lower_point_little_grid_1[0]+
                             num_of_columns*height_of_little_gap))/2

            textLocation_y = (upper_point_little_grid_1[1]+
                              lower_point_little_grid_1[1])/2

            textInt = board[num_of_rows][num_of_columns]

            canvas.create_text(textLocation_x, textLocation_y, text=textInt,
                       fill="purple", font="Helvetica 10 bold underline")   

def createSubboard(board, rowNum, columnNum):
    dimension = int(len(board[0])**0.5)
    subBoard  = []
    subRow    = []
    
    for num_of_rows_int in range(dimension):
        for num_of_columns_int in range(dimension):
            subRow.append(board[num_of_rows_int+rowNum*dimension]
                          [num_of_columns_int+columnNum*dimension])
        subBoard.append(subRow)
        subRow = []

    return subBoard

def drawSudokuBoard(canvas, width, height, board, margin):
    #canvas.create_text(width//2, height//2,
    #    text="Implement drawSudokuBoard!", font="Arial 20 bold")

    # === Parameters' definitions ===
    # width : the width of the window
    # height: the height of the window
    # board : NxN integers
    # margin: distance between the grid and the edge of the screen
    
    # === Features ===
    N = len(board)

    width_of_the_grid  = width  - 2*margin
    height_of_the_grid = height - 2*margin

    width_of_big_gap   = width_of_the_grid/(N**0.5)
    height_of_big_gap  = height_of_the_grid/(N**0.5)

    # === Create Frame ===
    upper_point_frame  = (margin, margin)
    lower_point_frame  = (width-margin, height-margin)
    canvas.create_rectangle(margin, margin, width-margin, height-margin)

    # === Create Big Grid ===

    for num_of_rows in range(int(N**0.5)):
        upper_point_big_grid_1 = (margin, margin+num_of_rows*width_of_big_gap)
        lower_point_big_grid_1 = (margin+width_of_big_gap
                               , (margin+height_of_big_gap)+
                               num_of_rows*width_of_big_gap)
        canvas.create_rectangle(upper_point_big_grid_1[0],
                                upper_point_big_grid_1[1],
                                lower_point_big_grid_1[0],
                                lower_point_big_grid_1[1],
                                outline="black", 
                                width=2)

        subBoard = createSubboard(board, num_of_rows, 0)
        
        drawLittleGrid(canvas, upper_point_big_grid_1, lower_point_big_grid_1, 
                      int(N**0.5), subBoard)
        
        for num_of_columns in range(int(N**0.5)):
            upper_point_big_grid = (upper_point_big_grid_1[0]+
                                    num_of_columns*height_of_big_gap,
                                    upper_point_big_grid_1[1])
            lower_point_big_grid = (lower_point_big_grid_1[0]+
                                    num_of_columns*height_of_big_gap,
                                    lower_point_big_grid_1[1])

            canvas.create_rectangle(upper_point_big_grid[0],
                                    upper_point_big_grid[1],
                                    lower_point_big_grid[0],
                                    lower_point_big_grid[1],
                                    outline="black", 
                                    width=2)

            subBoard = createSubboard(board, num_of_rows, num_of_columns)

            drawLittleGrid(canvas, upper_point_big_grid, lower_point_big_grid, 
                          int(N**0.5), subBoard)
        
def drawChessBoard(canvas, width, height, board, color, margin):
    canvas.create_text(width//2, height//2,
        text="Implement drawChessBoard!", font="Arial 20 bold")

#################################################################
# Test Functions
# Note: You must look at the output of these and confirm
# they work visually.
# You are not required to write tests for any helper functions
# you write for graphics problems
#################################################################

def getSudokuBoard0():
    return [
      [ 1, 2, 3, 4, 5, 6, 7, 8, 9],
      [ 5, 0, 8, 1, 3, 9, 6, 2, 4],
      [ 4, 9, 6, 8, 7, 2, 1, 5, 3],
      [ 9, 5, 2, 3, 8, 1, 4, 6, 7],
      [ 6, 4, 1, 2, 9, 7, 8, 3, 5],
      [ 3, 8, 7, 5, 6, 4, 0, 9, 1],
      [ 7, 1, 9, 6, 2, 3, 5, 4, 8],
      [ 8, 6, 4, 9, 1, 5, 3, 7, 2],
      [ 2, 3, 5, 7, 4, 8, 9, 1, 6]
    ]

def getSudokuBoard1():
    return [
        [1,2,3,4],
        [3,4,5,6],
        [7,8,9,10],
        [11,12,13,14]
    ]

def getStandardChessBoard():
    return [
        ['♜','♞','♝','♛','♚','♝','♞','♜'],
        ['♟','♟','♟','♟','♟','♟','♟','♟'],
        [' ']*8,
        [' ']*8,
        [' ']*8,
        [' ']*8,
        ['♙','♙','♙','♙','♙','♙','♙','♙'],
        ['♖','♘','♗','♕','♔','♗','♘','♖']
    ]

def getSimplifiedChessBoard():
    return [
        ['♜','♞','♝','♛','♚','♝','♞','♜'],
        ['♟','♟','♟','♟','♟','♟','♟','♟'],
        [' ']*8,
        [' ']*8,
        [' ']*8,
        ['♙','♙','♙','♙','♙','♙','♙','♙'],
        ['♖','♘','♗','♕','♔','♗','♘','♖']
    ]

def getSolitaireChessBoard():
    return [
        [' ']*4,
        [' ','♝',' ',' '],
        ['♜','♟',' ',' '],
        [' ',' ',' ','♞'],
    ]

def testDrawSudoku():
    print("Testing drawSudokuBoard()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    basic_graphics.run(getSudokuBoard0(), 10, drawFn=drawSudokuBoard)
    basic_graphics.run(getSudokuBoard1(), 10, drawFn=drawSudokuBoard)
    print("Done!")

def testDrawChessBoard():
    print("Testing drawChessBoard()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    basic_graphics.run(getStandardChessBoard(), (0,112,255), 20,
        drawFn=drawChessBoard,width=500,height=500
    )
    basic_graphics.run(getSolitaireChessBoard(), (255,150,0), 0,
        drawFn=drawChessBoard,width=150,height=150
    )
    basic_graphics.run(getSimplifiedChessBoard(), (10,255,0), 30,
        drawFn=drawChessBoard,width=300,height=260
    )
    print("Done!")



#################################################
# testAll and main
#################################################


def testAll():
    testDrawSudoku()
    #testDrawChessBoard()

def main():
    cs112_m20_unit6_linter.lint()
    testAll()

if __name__ == "__main__":
    main()

