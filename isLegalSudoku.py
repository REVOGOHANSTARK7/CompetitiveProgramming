'''
isLegalSudoku(board)
Write a function isLegalSudoku(board) that takes a n**2 x n**2 board where n is an odd number and return True  if this board is a legal sudoku 
and False otherwise.

Hint:
areLegalValues(values): This function takes a 1d list of values, which you should verify is of length N2 for some positive integer N and contains 
only integers in the range 0 to N2 (inclusive). These values may be extracted from any given row, column, or block in a Sudoku board (and, in fact, 
that is exactly what the next few functions will do -- they will each call this helper function). The function returns True if the values are legal: 
that is, if every value is an integer between 0 and N2, inclusive, and if each integer from 1 to N2 occurs at most once in the given list (0 may 
be repeated, of course). Note that this function does not take a 2d Sudoku board, but only a 1d list of values that presumably have been extracted 
from some Sudoku board.

isLegalRow(board, row): This function takes a Sudoku board and a row number. The function returns True if the given row in the given board is 
legal (where row 0 is the top row and row (N2-1) is the bottom row), and False otherwise. To do this, your function must create a 1d list of length 
N2 holding the values from the given row, and then provide these values to the areLegalValues function you previously wrote. (Actually, because 
areLegalValues is non-destructive, you do not have to copy the row; you may use an alias.)

isLegalCol(board, col): This function works just like the isLegalRow function, only for columns, where column 0 is the leftmost column and column 
(N2-1) is the rightmost column. Similarly to isLegalRow, this function must create a 1d list of length N2 holding the values from the given column, 
and then provide these values to the areLegalValues function you previously wrote.

isLegalBlock(board, block): This function works just like the isLegalRow function, only for blocks, where block 0 is the left-top block, and block 
numbers proceed across and then down, as described earlier. Similarly to isLegalRow and isLegalCol, this function must create a 1d list of length 
N2 holding the values from the given block, and then provide these values to the areLegalValues function you previously wrote.

isLegalSudoku(board): This function takes a Sudoku board (which you may assume is a N2xN2 2d list of integers), and returns True if the board is 
legal, as described above. To do this, your function must call isLegalRow over every row, isLegalCol over every column, and isLegalBlock over every \
    block. See how helpful those helper functions are? Seriously, this exercise is a very clear demonstration of the principle of top-down design 
    and function decomposition.
'''

'''
    This function takes a 1d list of values, which you should verify is of length N2 for some positive integer N and contains only integers in the range 0 to N2 (inclusive). These values may be extracted from any given row, column, or block in a Sudoko board (and, in fact, that is exactly what the next few functions will do -- they will each call this helper function). The function returns True if the values are legal: that is, if every value is an integer between 0 and N2, inclusive, and if each integer from 1 to N2 occurs at most once in the given list (0 may be repeated, of course). Note that this function does not take a 2d Sudoku board, but only a 1d list of values that presumably have been extracted from some Sudoku board.
'''
def areLegalValues(values):
    for i in range(len(values)):
        if(values[i]>9 or values[i]<0):
            return False
        if(values[i] in values[i+1:] and values[i]!=0):
            return False
        
    return True

'''
    This function takes a Sudoku board and a row number. The function returns True if the given row in the given board is legal 
    (where row 0 is the top row and row (N2-1) is the bottom row), and False otherwise. To do this, your function must create a 1d list 
    of length N2 holding the values from the given row, and then provide these values to the areLegalValues function you previously wrote. 
    (Actually, because areLegalValues is non-destructive, you do not have to copy the row; you may use an alias.)
'''
def isLegalRow(board, row):
    if(row>len(board)-1):
        return False
    return(areLegalValues(board[row]))
    
'''
    This function works just like the isLegalRow function, only for columns, where column 0 is the leftmost column and column (N2-1) 
    is the rightmost column. Similarly to isLegalRow, this function must create a 1d list of length N2 holding the values from the given column, 
    and then provide these values to the areLegalValues function you previously wrote.
'''
def isLegalCol(board, col):
    temp=[]
    if(col>len(board)-1):
        return False
    for i in range(len(board)):
        temp.append(board[i][col])
        
    
    return(areLegalValues(temp))


'''
    This function works just like the isLegalRow function, only for blocks, where block 0 is the left-top block, and block numbers proceed 
    across and then down, as described earlier. Similarly to isLegalRow and isLegalCol, this function must create a 1d list of length N2 holding 
    the values from the given block, and then provide these values to the areLegalValues function you previously wrote.
'''
def isLegalBlock(board, block):
    temp=[]
    if(block>len(board)-1):
        return False
    else:
        row=(block//3)*3
        col=(block*3)%9
        for i in range(row,row+3):
            for j in range(col,col+3):
                temp.append(board[i][j])
        print(temp)
        return(areLegalValues(temp))
    

'''
    This function takes a Sudoku board (which you may assume is a N2xN2 2d list of integers), and returns True if the board is legal, as 
    described above. To do this, your function must call isLegalRow over every row, isLegalCol over every column, and isLegalBlock over every block. 
    See how helpful those helper functions are? Seriously, this exercise is a very clear demonstration of the principle of top-down design and 
    function decomposition.
'''
def isLegalSudoku(board):
    for i  in range(len(board)):
        r=isLegalRow(board,i)
        c=isLegalCol(board,i)
        b=isLegalBlock(board,i)
    if(r==c and r==b and r==True):
        return True
    return False

print("Checking isLegalSudoku....")

true_board = [
            [1,2,3,4,5,6,7,8,9],
            [5,7,8,1,3,9,6,2,4],
            [4,9,6,8,7,2,1,5,3],
            [9,5,2,3,8,1,4,6,7],
            [6,4,1,2,9,7,8,3,5],
            [3,8,7,5,6,4,2,9,1],
            [7,1,9,6,2,3,5,4,8],
            [8,6,4,9,1,5,3,7,2],
            [2,3,5,7,4,8,9,1,6]
        ]

assert isLegalSudoku(true_board) == True

false_board = [
            [1,2,3,4,5,6,7,8,9],
            [5,7,8,1,3,9,6,2,4],
            [4,9,6,8,7,2,1,5,3],
            [9,5,2,3,8,1,4,6,7],
            [6,4,1,2,9,7,8,3,5],
            [3,8,7,5,6,4,2,9,1],
            [7,1,9,6,2,3,5,4,8],
            [8,6,4,9,1,5,3,7,2],
            [2,3,5,7,4,8,9,1,2]
        ]
assert isLegalSudoku(false_board) == False


valid_board1 = [[2, 7, 4, 1, 6, 8, 9, 3, 5], [8, 1, 6, 3, 9, 5, 4, 7, 2], [5, 3, 9, 7, 4, 2, 6, 1, 8], [4, 2, 3, 8, 7, 6, 1, 5, 9], [9, 5, 1, 2, 3, 4, 7, 8, 6], [6, 8, 7, 5, 1, 9, 3, 2, 4], [3, 4, 5, 6, 2, 7, 8, 9, 1], [7, 6, 2, 9, 8, 1, 5, 4, 3], [1, 9, 8, 4, 5, 3, 2, 6, 7]]
valid_board2 = [[7, 5, 2, 6, 9, 8, 4, 1, 3], [6, 9, 8, 4, 1, 3, 7, 5, 2], [4, 1, 3, 7, 5, 2, 6, 9, 8], [1, 2, 4, 5, 8, 7, 9, 3, 6], [9, 3, 6, 1, 2, 4, 5, 8, 7], [5, 8, 7, 9, 3, 6, 1, 2, 4], [2, 7, 1, 8, 6, 5, 3, 4, 9], [3, 4, 9, 2, 7, 1, 8, 6, 5], [8, 6, 5, 3, 4, 9, 2, 7, 1]]
assert isLegalSudoku(valid_board1) == True
assert isLegalSudoku(valid_board2) == True

print("All test cases passed...")
        