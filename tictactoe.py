#tic-tac-toe
#assigment 1
#udemy complete python bootcamp

board = [["x", "", ""], ["", "x", ""], ["", "", "x"]]

def printBoard():
    print("   1  2  3")
    i = 0
    for row in board:
        line = ""
        i += 1
        for col in row:
            line += " " + (col or " ") + " "
        print(i, line)
    print("")


def getInput(player):
    question = "Player " + player + " Enter Column :"
    column = input(question)
    if (column == "x"):
        print("You Quit!!")
        exit()

    question = "Enter Row :"
    row = input(question)
    if row == "x":
        print("You quit!")
        exit()
    irow = int(row) - 1
    icol = int(column) - 1
    if board[irow][icol] == "":
        board[int(row) - 1][int(column) - 1] = player
    else:
        print("That's an invalid entry")
        getInput(player)


def reset():
    for i in range(3):
        for j in range(3):
            board[i][j] = ""


def welcome():
    print("WELCOME TO TIC-TAC-TOE")


def changeTurn(player):
    if player == "X":
        return "0"
    return "X"


def checkRows(player):
    for row in board:
        if row == [player, player, player]:
            return True


def checkCols(player):
    for i in range(3):
        if [board[0][i], board[1][i], board[2][i]] == [player, player, player]:
            return True


def checkCross(player):
    if [board[0][0], board[1][1], board[2][2]] == [player, player, player]:
        return True
    if [board[0][2], board[1][1], board[2][0]] == [player, player, player]:
        return True



def anyPlayerWon():
    # check if any player won
    for player in ["0","X"]:
        if checkRows(player) or checkCols(player) or checkCross(player):
            print("Player",player,"won! Congratulations!")
            return True


def anyMoreTurns():
    for row in board:
        for col in row:
            if col == "":
                return True

def shouldContinue():
    answer = input("Do you want to play a new game? Y/n").upper()
    if not answer or answer == "Y":
        return True


def playGame():
    currentPlayer = "X"
    playing = True
    welcome()
    reset()
    printBoard()
    while playing:
        currentPlayer = changeTurn(currentPlayer)
        getInput(currentPlayer)
        printBoard()
        if anyPlayerWon():
            if shouldContinue():
                reset()
                printBoard()
            else:
                print("Game Over")
                exit()
        elif not anyMoreTurns():
            print("Game Tied")
            if shouldContinue():
                reset()
                printBoard()
            else:
                print("Game Over")
                exit()


playGame()
