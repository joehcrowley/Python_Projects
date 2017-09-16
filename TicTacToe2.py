from random import randint


def resetboard():
    global board
    board = list("   |   |   \n-----------\n   |   |   \n-----------\n   |   |   \n\n")



def map():
    map = list(" 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9 \n\n")
    print(''.join(map))

def checkwin():
    global turnstate
    global turnCounter
    if turnstate:
        if board[1] == "X":
            if board[5] == "X":
                if board[9] == "X":
                    print("You win!")
                    turnCounter = 11
            if board[25] == "X":
                if board[49] == "X":
                    print("You win!")
                    turnCounter = 11
            if board[29] == "X":
                if board[57] == "X":
                    print("You win!")
                    turnCounter = 11
        if board[29] == "X":
            if board[25] == "X":
                if board[33] == "X":
                    print("You win!")
                    turnCounter = 11
            if board[5] == "X":
                if board[53] == "X":
                    print("You win!")
                    turnCounter = 11
            if board[49] == "X":
                if board[9] == "X":
                    print("You win!")
                    turnCounter = 11
        if board[57] == "X":
            if board[33] == "X":
                if board[9] == "X":
                    print("You win!")
                    turnCounter = 11
            if board[49] == "X":
                if board[53] == "X":
                    print("You win!")
                    turnCounter = 11
    else:
        if board[1] == "O":
            if board[5] == "O":
                if board[9] == "O":
                    print("I win!")
                    turnCounter = 11
            if board[25] == "O":
                if board[49] == "O":
                    print("I win!")
                    turnCounter = 11
            if board[29] == "O":
                if board[57] == "O":
                    print("I win!")
                    turnCounter = 11
        if board[29] == "O":
            if board[25] == "O":
                if board[33] == "O":
                    print("I win!")
                    turnCounter = 11
            if board[5] == "O":
                if board[53] == "O":
                    print("I win!")
                    turnCounter = 11
            if board[49] == "O":
                if board[9] == "O":
                    print("I win!")
                    turnCounter = 11
        if board[57] == "O":
            if board[33] == "O":
                if board[9] == "O":
                    print("I win!")
                    turnCounter = 11
            if board[49] == "O":
                if board[53] == "O":
                    print("I win!")
                    turnCounter = 11


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
    else:
        if turnstate:
            print("Already taken, try again.")

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
    else:
        if turnstate:
            print("Already taken, try again.")

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
    else:
        if turnstate:
            print("Already taken, try again.")

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
    else:
        if turnstate:
            print("Already taken, try again.")

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
    else:
        if turnstate:
            print("Already taken, try again.")

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
    else:
        if turnstate:
            print("Already taken, try again.")

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
    else:
        if turnstate:
            print("Already taken, try again.")

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
    else:
        if turnstate:
            print("Already taken, try again.")

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
    else:
        if turnstate:
            print("Already taken, try again.")

play = True
while(play == True):

    global board
    resetboard()
    global turnCounter
    global turnstate
    turnCounter = 0

    print("Welcome to TicTacToe!")

    #Game start, decides who goes first
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

    while turnCounter < 10:
        #Player moves
        if turnstate:
            move = input("Please enter where you would like to go.\n")
            if move == "1":
                topleft()
            elif move == "2":
                topmiddle()
            elif move == "3":
                topright()
            elif move == "4":
                leftmiddle()
            elif move == "5":
                middle()
            elif move == "6":
                rightmiddle()
            elif move == "7":
                bottomleft()
            elif move == "8":
                bottommiddle()
            elif move == "9":
                bottomright()
        #Computer moves
        else:
            print("My turn!\n")
            if turnCounter < 3:
                if board[29] == " ":
                    middle()
                else:
                    topleft()
             #Checks if opponent will win in top row
            if board[1] == "X":
                if board[5] == "X":
                    topright()
                if board[9] == "X":
                    topmiddle()
            if board[9] == "X":
                if board[5] == "X":
                    topleft()
            #Checks if opponent will win in left column
            if board[1] == "X":
                if board[25] == "X":
                    bottomleft()
                if board[49] == "X":
                    leftmiddle()
            if board[49] == "X":
                if board[25] == "X":
                    topleft()
            # Checks if opponent will win on positive diagonal
            if board[9] == "X":
                if board[29] == "X":
                    bottomright()
                if board[49] == "X":
                    middle()
            if board[49] == "X":
                if board[29] == "X":
                    topright()
            # Checks if opponent will win in middle row
            if board[25] == "X":
                if board[29] == "X":
                    rightmiddle()
                if board[33] == "X":
                    middle()
            if board[33]:
                if board[29] == "X":
                    leftmiddle()
            # Checks if opponent will win in middle column
            if board[5] == "X":
                if board[29] == "X":
                    bottommiddle()
                if board[53] == "X":
                    middle()
            if board[53] == "X":
               if board[29] == "X":
                   topmiddle()
            # Checks if opponent will win right column
            if board[9] == "X":
                if board[33] == "X":
                    bottomright()
                if board[57] == "X":
                    rightmiddle()
            if board[57] == "X":
                if board[33] == "X":
                    topright()
            # Checks if opponent will win in bottom row
            if board[49] == "X":
                if board[53] == "X":
                    bottomright()
                if board[57] == "X":
                    bottommiddle()
            if board[57] == "X":
                if board[53] == "X":
                    bottomleft()
        print(''.join(board))
    #End of Game, ADD CAT'S GAME
    if turnCounter >= 10:
        if turnCounter == 10:
            print("Cat's game, better play another one!\n")
        replay = input("Would you like to play again? Y/N\n")
        if replay == "N":
            print("Thanks for playing, come back sometime!\n")
            play = False

