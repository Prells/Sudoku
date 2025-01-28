import pickle
from tkinter import * 

class Sudoku (object):
    def __init__(self, fileName):
        self.fileName = fileName
        self.sudokuBoard = [[0 for i in range(9)] for j in range(9)]
        print(self.sudokuBoard)
        
    def readFile(self):
        try:
            fileSudoku = open(self.fileName, "r")
            i = 0
            for strLine in fileSudoku:
                j = 0
                for ch in strLine:
                    self.sudokuBoard[i][j] = ch
                    j+= 1
                    if j == 9:
                        break
                i+= 1
                if i == 9:
                    break
            print(self.sudokuBoard)
            return self.sudokuBoard
        except(IOError):
            print("Error opening/reading {}".format(self.fileName))
            quit()

class myWindow(Frame):
    #Creates the initial window with 2 buttons to open a file and a 2D array to store the file information
    def __init__(self, master=None):
        self.toplevel=master
        Frame.__init__(self,master)        
        self.sudokuEntries = [[0 for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                self.sudokuEntries[i][j] = StringVar()
        self.btnCheck = Button(text="Check Solution", command=self.checkBoard)
        self.btnCheck.pack(side = TOP)
        self.btnFile = Button(text="Open File", command=self.openFile)
        self.btnFile.pack(side = TOP)

    #Algorithm to check if the board is in a solved state, turns the square green if correct and red if incorrect    
    def checkBoard(self):
        for entry in self.lstEntries:
            if entry == ' ':
                print(0)
            else:
                print(entry.get())
        
    #Method to create a Sudoku board, sudoku is a 2D array of String Vars contain a text version of Sudoku
    def createBoard(self, sudoku):
        print(sudoku)
        self.lstEntries = []
        #Creates a Frame for each row
        for i in range(9):
            sudokuFrame = Frame(myGui, height=100, width=900)
            sudokuFrame.pack(side = TOP)
            #Creates a square in the frame and displays a number if given
            for j in range(9):
                box = Frame(sudokuFrame, width=100, height=100)
                box.pack_propagate(False)
                strVar = StringVar()
                self.entry = Entry(box, textvariable=strVar, justify=CENTER, font="Arial 12")
                self.entry.place(height=100, width=100)
                self.lstEntries.append(strVar)
                if sudoku[i][j] != '0':
                    strVar.set(sudoku[i][j])
                box.pack(side = LEFT)
                
               

    #Creates a window to enter a file name containing a Sudoku Board
    def openFile(self):
        self.newWindow = Toplevel(self.toplevel)
        self.newWindow.title("Open File")
        self.newWindow.geometry("200x200")
        self.fileEntry = Entry(self.newWindow, font="Arial 12")
        self.fileEntry.pack()
        Button(self.newWindow, text="Open", command=self.readFile).pack()

    #Reads the given File and creates the Sudoku Board
    def readFile(self):
        strFile = self.fileEntry.get()
        sudokuFile = Sudoku(strFile)
        sudoku = sudokuFile.readFile()
        self.createBoard(sudoku)
        self.newWindow.destroy()
        
myGui = Tk()
myForm=myWindow(myGui)
myForm.master.title("Sudoku")
myGui.mainloop()




    
