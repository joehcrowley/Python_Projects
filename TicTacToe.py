from random import randint


def resetboard():
    # board = [[" ", " ", " ", "|", " ", " ", " ", "|"," ", " ", " "], ["-","-","-","-","-","-","-","-","-","-",], [" ", " ", " ", "|", " ", " ", " ", "|"," ", " ", " "], ["-","-","-","-","-","-","-","-","-","-",], [" ", " ", " ", "|", " ", " ", " ", "|"," ", " ", " "] ]
    board = list("   |   |   \n-----------\n   |   |   \n-----------\n   |   |   \n\n")
    print(board)


def map():
    map = list(" 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9 \n\n")
    print(''.join(map))


def topleft():
    global turnstate
    if board[1] == " ":
        if turnstate:
            board[1] = "X"
        elif not turnstate:
            board[1] = 'O'
        global turnCounter
        turnCounter += 1
        turnstate = not turnstate

def topmiddle():
    global turnstate
    if board[5] == " ":
        if turnstate:
            board[5] = "X"
        elif not turnstate:
            board[5] = 'O'
        global turnCounter
        turnCounter += 1
        turnstate = not turnstate

def topright():
    global turnstate
    if board[9] == " ":
        if turnstate:
            board[9] = "X"
        elif not turnstate:
            board[9] = 'O'
        global turnCounter
        turnCounter += 1
        turnstate = not turnstate

def leftmiddle():
    global turnstate
    if board[25] == " ":
        if turnstate:
            board[25] = "X"
        elif not turnstate:
            board[25] = 'O'
        global turnCounter
        turnCounter += 1
        turnstate = not turnstate

def middle():
    global turnstate
    if board[29] == " ":
        if turnstate:
            board[29] = "X"
        elif not turnstate:
            board[29] = 'O'
        global turnCounter
        turnCounter += 1
        turnstate = not turnstate

def rightmiddle():
    global turnstate
    if board[33] == " ":
        if turnstate:
            board[33] = "X"
        elif not turnstate:
            board[33] = 'O'
        global turnCounter
        turnCounter += 1
        turnstate = not turnstate

def bottomleft():
    global turnstate
    if board[49] == " ":
        if turnstate:
            board[49] = "X"
        elif not turnstate:
            board[49] = 'O'
        global turnCounter
        turnCounter += 1
        turnstate = not turnstate

def bottommiddle():
    global turnstate
    if board[53] == " ":
        if turnstate:
            board[53] = "X"
        elif not turnstate:
            board[53] = 'O'
        global turnCounter
        turnCounter += 1
        turnstate = not turnstate

def bottomright():
    global turnstate
    if board[57] == " ":
        if turnstate:
            board[57] = "X"
        elif not turnstate:
            board[57] = 'O'
        global turnCounter
        turnCounter += 1
        turnstate = not turnstate




board = list("   |   |   \n-----------\n   |   |   \n-----------\n   |   |   \n\n")
turnCounter = 0

print("Welcome to TicTacToe!")

while turnCounter == 0:
    turn = input("Do you want to go first? Y/N/RANDOM\n")
    if turn == 'Y':
        print("You are going first!\n")
        turnCounter += 1
        turnstate = True
    elif turn == 'N':
        print("You are going second!\n")
        turnCounter += 1
        turnstate = False
    elif turn == 'RANDOM':
        turn = randint(0, 1)
        if turn == 0:
            print("You are going first!\n")
            turnCounter += 1
            turnstate = True
        else:
            print("You are going second!\n")
            turnCounter += 1
            turnstate = False
    else:
        print("Please only enter Y/N/RANDOM.\n")

map()

while turnCounter < 9:
    if turnstate:
        move = input("Please enter where you would like to go.\n")
        if move == "1":
            if board[1] == " ":
                board[1] = "X"
                turnCounter += 1
                turnstate = False
        elif move == "2":
            if board[5] == " ":
                board[5] = "X"
                turnCounter += 1
                turnstate = False
        elif move == "3":
            if board[9] == " ":
                board[9] = "X"
                turnCounter += 1
                turnstate = False
        elif move == "4":
            if board[25] == " ":
                board[25] = "X"
                turnCounter += 1
                turnstate = False
        elif move == "5":
            if board[29] == " ":
                board[29] = "X"
                turnCounter += 1
                turnstate = False
        elif move == "6":
            if board[33] == " ":
                board[33] = "X"
                turnCounter += 1
                turnstate = False
        elif move == "7":
            if board[49] == " ":
                board[49] = "X"
                turnCounter += 1
                turnstate = False
        elif move == "8":
            if board[53] == " ":
                board[53] = "X"
                turnCounter += 1
                turnstate = False
        elif move == "9":
            if board[57] == " ":
                board[57] = "X"
                turnCounter += 1
                turnstate = False
        print(''.join(board))
    else:
        print("My turn!\n")
        if turnCounter < 3:
            if board[29] == " ":
                board[29] = "O"
                turnCounter += 1
                turnstate = True
            else:
                board[1] = "O"
                turnCounter += 1
                turnstate = True

        print(''.join(board))
