class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def playTicTacToe():
    rows,cols = 3,3
    winLength = 3
    board = makeNewBoard(rows, cols)
    moves = 0
    player = 1

    while moves < rows*cols:
        row,col = getMove(board, player)
        board = setPiece(board, row, col, player)
        if (didWin(board, player, winLength)):
            printBoard(board)
            print("")
            #print '%s   The Player %s  color.GREEN + color.Bold + "-->" + color.END, """ won the game!""" + color.END % (color.GREEN,getPieceLabel(player),
            print(color.RED + color.BOLD + "The Player" + color.END, getPieceLabel(player), color.RED + color.BOLD + "won the game! " + color.END)
            return
        player = otherPlayer(player)
        moves += 1
    print(color.RED + color.BOLD + "TIE GAME!" + color.END)


def makeNewBoard(rows, cols):
    return [([0]*cols) for row in range(rows)]


def getRows(board):
    return len(board)

def getCols(board):
    return len(board[0])

def getPiece(board, row, col):
    return board[row][col]

def setPiece(board, row, col, value):
    board[row][col] = value
    return board

def isEmpty(board, row, col):
    return (getPiece(board, row, col) == 0)

def isOnBoard(board, row, col):
    rows = getRows(board)
    cols = getCols(board)
    return ((row >= 0) and (row < rows) and
            (col >= 0) and (col < cols))

def getPieceLabel(piece):
    if (piece == 1):
        return "|" + color.PURPLE + color.BOLD + "X" + color.END + "|"
    elif (piece == 2):
        return "|" + color.BLUE + color.BOLD + "O" + color.END + "|"
    else:
        return color.BOLD + "|_|" + color.END

def printBoard(board):
    print("\n")
    rows = getRows(board)
    cols = getCols(board)
    for row in range(rows):
        for col in range(cols):
            piece = getPiece(board, row, col)
            label = getPieceLabel(piece)
            print(label, end=' ')
        print()


def didWin(board, player, winLength):
    rows = getRows(board)
    cols = getCols(board)
    for startRow in range(rows):
        for startCol in range(cols):
            if (didWin1(board, player, winLength, startRow, startCol)):
                return True
    return False

def didWin1(board, player, winLength, startRow, startCol):
    for drow in range(-1,+2):
        for dcol in range(-1,+2):
            if ((drow != 0) or (dcol != 0)):
                if (didWin2(board, player, winLength,
                            startRow, startCol, drow, dcol)):
                    return True
    return False

def didWin2(board, player, winLength,
            startRow, startCol, drow, dcol):
    rows = getRows(board)
    cols = getCols(board)
    for step in range(winLength):
        row = startRow + step*drow
        col = startCol + step*dcol
        if (not isOnBoard(board, row, col)):
            return False
        elif (getPiece(board, row, col) != player):
            return False
    return True


def otherPlayer(player):
    return 1 if (player == 2) else 2


def oops(msg):
    print("  ", msg, color.RED + color.BOLD + "Try again." + color.END)


def readInt(prompt):
    while True:
        try:
            return int(input(prompt))
        except TypeError:
            oops(color.RED + color.BOLD + "Input must be an integer." + color.END)

def getMove(board, player):
    while True:
        printBoard(board)
        print("Enter move for player:" + getPieceLabel(player))
        row = readInt("  Row --> ") - 1
        col = readInt("  Col --> ") - 1
        if (not isOnBoard(board, row, col)):
            oops(color.RED + color.BOLD + """\n \n Out of range (not on the board)!""" + color.END)
        elif (not isEmpty(board, row, col)):
            oops(color.RED + color.BOLD +"""\n The opponent already occupied this place!""" + color.END)
        else:
            return (row, col)


def finish():
    answer = input(color.PURPLE + color.BOLD + """Would you like to play again?! (press \'y\' for yes and \'n\' for no):""" + color.END)
    if answer.lower() == "n":
        print("")
        print(color.BLUE + color.BOLD + "Okay, see you next time." + color.END)
        return True
    if answer.lower() == "y":
        print((color.BLUE + color.BOLD + """\nOkay, game will start again!""" + color.END))
        return False












def main():
    while True:
        playTicTacToe()
        if finish():
            break








if __name__ == '__main__':
    main()
