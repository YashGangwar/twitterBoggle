import csv
import numpy
import os

boardFile = "../DataFiles/"
englishDict= "../DataFiles/"

# recursive function to search for word within boggle board
def recCheck(brd, word, vst, i, j):
    if i < 0 or j < 0 or i >= y or j >= x:
        return False
    if vst[i][j] == 0 and len(word) == 1 and (brd[i][j] == "*" or word[0].upper() == brd[i][j].upper()):
        vst[i][j] = 1
        return True
    else:
        if vst[i][j] == 1:
            return False
        if brd[i][j] == '*' or word[0].upper() == brd[i][j].upper():
            vst[i][j] = 1
            return (recCheck(brd, word[1:], vst, i-1, j) or recCheck(brd, word[1:], vst, i+1, j) or recCheck(brd, word[1:], vst, i, j-1) or recCheck(brd, word[1:], vst, i, j+1)
                or recCheck(brd, word[1:], vst, i+1, j+1) or recCheck(brd, word[1:], vst, i+1, j-1) or recCheck(brd, word[1:], vst, i-1, j+1) or recCheck(brd, word[1:], vst, i-1, j-1))

# FIRST FUNCTION: Function validates whether given word is part of dictionary provided and searches for word within the boggle board provided
def findWord(brd, word, dict, vst):
    if word.lower() not in dict:    # Searching for word in dictionary
        print(word + " is not valid english word.\n")
        return False
    
    for i in range(y):
        for j in range(x):
            vst = numpy.array([[0]*x]*y)
            if brd[i][j] == "*" or brd[i][j].upper() == word[0].upper():
                # print("hello")
                if recCheck(brd, word, vst, i, j) == True:
                    return True
                else:
                    continue
    return False

# SECOND FUNCTION: Function returns a list of all possible words found in the board
def findAll(brd, dict, vst):
    collection = []
    for word in dict:
        if findWord(brd, word, dict, vst) == True:
            collection.append(word)
    return collection

# Function used to print the board in the terminal
def printBoard(brd):
    print("-----------------")
    for x in brd:
        print("|", end='')
        for y in x:
            print (" "+y+" |", end='')
        print("\n-----------------")

temp = 0
board = []

print("\nPlease store all boggle boards in DataFiles Directory")

# Taking board file name input. All boggle boards must be stored in DataFiles directory
while(temp == 0):
    boardFile = "../DataFiles/"
    boardInput = input("Enter file name for boggle board: ")
    boardFile = boardFile+boardInput
    if not os.path.exists(boardFile):
        print(boardFile)
        print("Invalid File name")
        continue
    with open(boardFile, "r") as value:
        reader = csv.reader(value, skipinitialspace=True)
        board = next(reader)
        if len(board)%4 != 0 or len(board)/4 <2:
            print("Entered Boggle board is not valid") 
            continue
    temp = 1

temp = 0
english = {}

print("\nPlease store all english dictionaries in DataFiles Directory")

# Taking english dictionary file name input. All english dictionary files must be stored in DataFiles directory
while(temp == 0):
    englishDict = "../DataFiles/"
    dictInput = input("Enter file name for English Dictionary: ")
    englishDict = englishDict+dictInput
    if not os.path.exists(englishDict):
        print("Invalid File name")
        continue
    with open(englishDict, "r") as eng:
        for line in eng:
            english[line[:-1]] = 1          #truncating new line character and saving in python dictionary
    temp = 1

# Considering a boggle board with size 4
x = 4
y = int(len(board)/4)

board = numpy.array(board).reshape(y,x)
printBoard(board)
visit = numpy.array([[0]*x]*y)
test = input("1. Check words\n2. Show all possible solutions\n")

# Testing the first function that finds word in boggle board and validates if the word is an english word
if test == "1":
    printBoard(board)
    while(True):
        testWord = input("Enter word: ")
        visit = numpy.array([[0]*x]*y)
        if findWord(board, testWord, english, visit):
            print(testWord + ": Correct Word")
        else:
            print(testWord + ": Wrong Word")

# Testing the second function that finds all the possible words found in the boggle board
elif test == "2":
    print("Processing...")
    findWords = findAll(board, english, visit)
    if len(findWords) == 0:
        print("No valid words found from dictionary "+dictInput)
        exit(0)
    print("Following are the correct words found from dictionary "+dictInput)
    print(findWords)
