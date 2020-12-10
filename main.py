
name_x = ''
name_O=''
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = 1

Win = 1
Draw = -1
Running = 0
Stop = 1

Game = Running
Mark = 'X'

def DrawBoard():
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print("---+---+---")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("---+---+---")
    print(" %c | %c | %c " % (board[1], board[2], board[3]))


def CheckPosition(x):
    if (board[x] == ' '):
        return True
    else:
        return False

def CheckWin():
    global Game
    if (board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        Game = Win
    elif (board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
        Game = Win
    elif (board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
        Game = Win

    elif (board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        Game = Win
    elif (board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        Game = Win
    elif (board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
        Game = Win
    elif (board[1] == board[5] and board[5] == board[9] and board[5] != ' '):
        Game = Win
    elif (board[3] == board[5] and board[5] == board[7] and board[5] != ' '):
        Game = Win
    elif (board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[
        6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' '):
        Game = Draw
    else:
        Game = Running


name_x = input("Enter 1st player name: ")
name_O = input("Enter 2nd player name: ")

print(name_x + ": X | " + name_O + ": O")


while (Game == Running):
    DrawBoard()

    if (player % 2 != 0):
        print("It's your turn, " + name_x + ". Move to which place?")
        Mark = 'X'
    else:
        print("It's your turn, " + name_O + ". Move to which place?")
        Mark = 'O'
    choice = int(input())
    if (CheckPosition(choice)):
        board[choice] = Mark
        player += 1
        CheckWin()

DrawBoard()
if (Game == Draw):
    print("\nGame Over.\n")
    print("It's a Tie!!")
elif (Game == Win):
    player -= 1
    if (player % 2 != 0):
        print(" **** " + name_x + " won ****")
    else:
        print(" **** " + name_O + "won ****")