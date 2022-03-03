#1 - Create display board
#2 - Take input from user (O or X)
#3 - Fill the user value on the board
#4 - Winning check
#5 - if the spot is empty
#6 - Deciding whose turn is first 
#7 - if the board is full
#8 - ask if the player wants to play again
#9 - initialise board
#10 - Compile and play



from IPython.display import clear_output
import random


#1 - Create display board

def display(board):
    clear_output()
    for i in range(3):
        print(board[3*i + 1] + '|' + board[3*i + 2] + '|' + board[3*i + 3])




#2 - Take input from user (O or X)

def TakeInput():
    temp=""
    while not (temp == 'X' or temp == 'O'):
        temp = input("Player 1: Enter your choice('O' or 'X'):").upper()
        
    if(temp=="O"):
        return "O","X"
    else:
        return "X","O"




#6 - Deciding whose turn is first 

def decideFirst():
    x = random.randint(0,2)
    return x




#8 - ask if the player wants to play again

def quit():
    temp = input("Want to quit?(y/n): ").lower()
    if(temp.startswith('y')):
        return True
    else:
        return False




#5 - if the spot is empty

def isSpotEmpty(position,board):
    if(board[position]==' '):
        return True
    else:
        return False




#3 - Fill the user value on the board

def fillValues(value,position,board):
    board[position]=value
    return board




#7 - if the board is full

def isBoardFull(board):
    
    for i in range(1,10):
        if(board[i]==' '):
            return False
            
    return True




#4 - Winning check

def checkWinner(board):
    
    tup = ("O","X")
    
    for val in tup:
        if((board[7]==val and board[8]==val and board[9]==val) or (board[7]==val and board[4]==val and board[1]==val) or 
           (board[7]==val and board[5]==val and board[3]==val) or (board[4]==val and board[5]==val and board[6]==val) or
           (board[8]==val and board[5]==val and board[2]==val) or (board[3]==val and board[2]==val and board[1]==val) or 
           (board[3]==val and board[6]==val and board[9]==val)):
            return val
    
    return " "



#9 - initialise board

def initialiseBoard(board):
    for i in range(0,10):
        board.append(" ")
        
    return board    



#10 - Input for position

def inputPosition(board):
    
    position = int(input("Enter the position you want to mark(0-9): "))
    while (position>0 and position <10) and (not isSpotEmpty(position,board)):
        print("Sorry, that position is already filled! Try again...")
        position = int(input("Enter the position you want to mark(0-9): "))
        
    return position    



#11 - Compile and play

def play(board):
    board = initialiseBoard(board)
    display(board)
    
    first,second = TakeInput()
    
    switch = decideFirst()
    if(switch==0):
        print("Player 1 will play first!")
        marker=first
    else:
        print("Player 2 will play first!")
        marker=second
    
    
    while isBoardFull(board)==False:
        
        if(switch==0):
            clear_output()
            print("Player 1: ",end=' ')
            position = inputPosition(board)
    
        else:
            clear_output()
            print("Player 2: ",end=' ')
            position = inputPosition(board)
            
        board = fillValues(marker,position,board)    
        
        if checkWinner(board)=="O" or checkWinner(board)=="X":
            if switch==0:
                clear_output()
                display(board)
                print("Player 1 won the game!!")
            else:
                clear_output()
                display(board)
                print("Player 2 won the game!!")
            break 
        
        display(board)
        switch = 1 - switch
        if (marker=="O"):
            marker = "X"
        else:
            marker = "O"

    
    if isBoardFull(board) and checkWinner(board)==" ":
        print("It's a draw!!")



#12 - main function

if __name__ == '__main__':
    board = []
    play(board)

    while not quit():
        board = []
        play(board)

    print("Thank you for playing the game!!")    