def Letter(letter,position):
    board[position] = letter

#Return a True Or False
def AvailableSpace(position):
    return board[position] == " "

def GameBoard(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print("")

def Winner(board, letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or
    (board[4] == letter and board[5] == letter and board[6] == letter) or
    (board[1] == letter and board[2] == letter and board[3] == letter) or
    (board[7] == letter and board[4] == letter and board[1] == letter) or
    (board[8] == letter and board[5] == letter and board[2] == letter) or
    (board[9] == letter and board[6] == letter and board[3] == letter) or
    (board[7] == letter and board[5] == letter and board[3] == letter) or
    (board[9] == letter and board[5] == letter and board[1] == letter))

def isBoardFull(board):
    #Counts the number of empty spaces
    #Gotta use >1 cuz used range(10)
    if board.count(" ") > 1:
        return False
    else:
        return True

def Player():
    move= True
    while move:
        pos=int(input("Select a position to place your X (1-9): "))
        if pos <10 or pos >0:
            if AvailableSpace(pos):
                move=False
                Letter("X",pos)
            else:
                print("This position is occupied!")
        else:
            print("Type a number between 1 and 9.")

def Randomizer(x):
    import random
    r=random.randrange(0,len(x))
    return x[r]


def Computer():
    possibleMoves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    move = 0

    for i in ['O', 'X']:
        for j in possibleMoves:
            BoardCopy = board[:]
            BoardCopy[j] = i
            if Winner(BoardCopy, i):
                move = j
                return move

    OpenCorners = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            OpenCorners.append(i)

    if len(OpenCorners) > 0:
        move = Randomizer(OpenCorners)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    OpenEdges = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            OpenEdges.append(i)
    if len(OpenEdges) > 0:
        move = Randomizer(OpenEdges)

    return move

def main():
    GameBoard(board)

    while not(isBoardFull(board)):
        if not(Winner(board, "O")):
            Player()
            GameBoard(board)
        else:
            print("Dude, You lost against a bot....")
            break

        if not(Winner(board, "X")):
            move = Computer()
            if move == 0:
                print("Tie Game!")
            else:
                Letter("O", move)
                GameBoard(board)
        else:
            print("You won against a bot, how do you feel?")
            break

    if isBoardFull(board):
        print("Tie Game!")

while True:
    ans = input("Do you want to play (Y/N): ")
    if ans.lower() == 'y':
        # Range is 10 to let users type 1-9 instead of 0-8
        board = [" " for x in range(10)]
        print("-----------------------------------")
        main()
    else:
        break