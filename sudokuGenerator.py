import random
import math
import pdb

class SudokuGenerator:
    def __init__(self):
        self.N = 9
        self.K = 9
        self.board = [[0 for i in range(self.N)] for j in range(self.N)]
        

    def generateBoard(self):
        self.fillDiags()
        #self.printBoard()
        self.fillEmptyCells()
        #self.checkAllBoxes()
        self.checkPuzzle()
        #self.checkRowsAndCols()

    def fillDiags(self):
        #0,0 to 2,2
        #3,3 to 5,5
        #6,6 to 8,8
        for i in range(3):
            self.fillBox(i*3 , i*3)
        
    def fillEmptyCells(self):
        lstNums = [1,2,3,4,5,6,7,8,9]
        for i in range(9):
            for j in range(9):
                num = random.randint(1,9)
                tempBoard = self.board[i][j]
                while lstNums[num-1] == 0:
                    num = random.randint(1, 9)
                if self.board[i][j] == 0:
                    for k in range(9):
                        boolRow = self.checkRow(i, j, num)
                        boolCol = self.checkCol(i, j, num)
                        boolBox = self.checkBox(math.floor(i/3), math.floor(j/3), num)
                        if boolRow and boolCol and boolBox:
                            self.board[i][j] = num
                            lstNums[num-1] = 0
                            break
                        elif boolRow == False or boolCol == False or boolBox == False:
                            self.backtrack(i, j, num)
                            
                        
    def backtrack(self, row, col, num):
        if self.checkRow(row, col, num) == False:
            for i in range(9):
                if self.board[row][i] == num and i != col:
                    
            
                    
        
    def checkCol(self, row, col, number):
        for i in range(9):
            if self.board[i][col] == number and i != row:
                return False
        return True

    def checkRow(self, row, col, number):
        for i in range(9):
            if self.board[row][i] == number and i != col:
                return False
        return True

             
    def checkBox(self, row, col, number):
        for i in range(3):
            for j in range(3):
                if self.board[row + i][col + j] == number:
                    return False
        return True
    
    def checkPuzzle(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    self.fillEmptyCells()
                    
    def fillBox(self, row, col):
        for i in range(3):
            for j in range(3):
                num = random.randint(1,9)
                while self.checkBox(row, col, num) == False:
                    num = random.randint(1,9)
                self.board[i+row][j+col] = num   
    
    def printBoard(self):
        for i in range(9):
            print(self.board[i])
        self.sendToFile()

    def sendToFile(self):
        try:
            fileSudoku = open("sudoku.txt", "w")
            for i in range(9):
                for(j) in range(9):
                    fileSudoku.write(str(self.board[i][j]))
                fileSudoku.write("\n")
        except(IOError):
            print("Error opening sudoku.txt")
            quit()

sudokuboard = SudokuGenerator()
sudokuboard.generateBoard()
sudokuboard.printBoard()
                    
