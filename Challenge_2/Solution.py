import csv
import numpy

# Files I'll be using. Board file and english Dictionary
boardFile = "../DataFiles/board2.txt"
englishDict= "../DataFiles/words_alpha.txt"

english = {}

# Saving english words in a python dictionary
with open(englishDict, "r") as eng:
    for line in eng:
        english[line[:-2]] = 1

# Saving board
board = []
with open(boardFile, "r") as value:
    reader = csv.reader(value, skipinitialspace=True)
    board = next(reader)
    


# removing all spaces and special characters
if len(board)%4 != 0:
    print("Hey WTF bruh") 
x = 4
y = int(len(board)/4)

print(numpy.array(board).reshape(y,x))
board = numpy.array(board).reshape(y,x)
visit = [[0]*x]*y

print(numpy.array(visit))

def recCheck(brd, word, vst, i, j):
    print(str(i)+ "-"+str(j)+": "+str(x)+" "+str(y)+":"+word)
    if i < 0 or j < 0 or i >= y or j >= x:
        print("Went out of bounds")
        return False
    if vst[i][j] == 0 and len(word) == 1 and word[0].upper() == brd[i][j].upper():
        print(vst)
        return True
    else:
        if vst[i][j] == 1:
            return False
        vst[i][j] = 1
        if brd[i][j] == '*' or word[0].upper() == brd[i][j].upper():
            return (recCheck(brd, word[1:], vst, i-1, j) or recCheck(brd, word[1:], vst, i+1, j) or recCheck(brd, word[1:], vst, i, j-1) or recCheck(brd, word[1:], vst, i, j+1)
                or recCheck(brd, word[1:], vst, i+1, j+1) or recCheck(brd, word[1:], vst, i+1, j-1) or recCheck(brd, word[1:], vst, i-1, j+1) or recCheck(brd, word[1:], vst, i-1, j-1))


def findWord(brd, word, dict, vst):
    if word not in dict:
        print("Entered word is not a valid english word")
        return False
    for i in range(y):
        for j in range(x):
            print(str(i)+ " "+str(j))
            # print(brd)
            if brd[i][j] == "*" or brd[i][j].upper() == word[0].upper():
                print("hello")
                if recCheck(brd, word, vst, i, j) == True:
                    return True
                else:
                    continue
    return False

print(findWord(board, "dug", english, visit))