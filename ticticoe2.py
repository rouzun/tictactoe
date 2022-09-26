def display_board(board):
    
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}  ")
    print(f"-----|-----|-----    ")
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}  ")
    print(f"-----|-----|-----")
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}  ")

def player_input():

    holder="wrong"
    while holder not in ["X","O","x","o"]:
        marker=input("Select O or X :")
        holder=marker
        if marker not in ["X","O","x","o"]:
            print("Only Select X or O!")
    return marker.upper()

def place_marker(board, marker, position):
    
    board[position]=marker

def win_check(board, mark):
    
    if board[1]==board[2]==board[3]==mark:
        winn=True
    elif board[4]==board[5]==board[6]==mark:
        winn=True
    elif board[7]==board[8]==board[9]==mark:
        winn=True
    elif board[1]==board[4]==board[7]==mark:
        winn=True
    elif board[2]==board[5]==board[8]==mark:
        winn=True
    elif board[3]==board[6]==board[9]==mark:
        winn=True
    elif board[3]==board[5]==board[7]==mark:
        winn=True
    elif board[1]==board[5]==board[9]==mark:
        winn=True
    else:
        winn=False                
    return winn

import random
from re import X

def choose_first():
    e=random.randint(1,2)
    if e==1:
        print ("Player 1 goes First")
    else:
        print ("Player 2 goes First")

def space_check(board, position):
    chkboard=[]
    e=False
    
   
    if board[position] in range(1,10):
        e=True
        
        
       
    return e

def full_board_check(board):
    e=True   
    
    for r in range(1,10):
        if r in board:
            e=False
            break
    return e

def player_choice(board):
    p="wrong"
    while not p.isdigit():
        
        p=input("Which position wanna place your mark(1-9) ")
        pp=p
        if p.isdigit()==False:
            print("Only 1-9 numbers please")
            continue
        elif int(p) not in range(1,10):
            print ("1 to 9 Please")
            p="wrong"
            continue
        elif space_check(board, int(p)) ==False:
            print("Taken")
            p="wrong"
    position=int(p)
    return position

def replay():
    choice="Wrong"
    while choice not in ["Y","y","N","n"]:
        choice=input("Wanna Play More? (Y or N) : ")
        if choice not in ["Y","y","N","n"]:
            print("Please only Y or N")
        elif choice in ["Y","y"]:
            return True
        elif choice in ["N","n"]:
            return False

import os

os.system('cls')

print('Welcome to Tic Tac Toe!')



while True:
    
    board1=[]
    for i in range (10):
        board1.append(i)
    os.system('cls')
    choose_first()
    mark=player_input()
    game_on=full_board_check(board1)
    
    while game_on==False:
        
        if mark=="X":
            
            os.system('cls')
            display_board(board1)
            
            print(mark+"'s Turn")
            #print(game_on)
            position=player_choice(board1)
            place_marker(board1, mark, position)
            if win_check(board1, mark)==True:
                
                os.system('cls')
                display_board(board1)
                
                print("X Won!!")
                break
            else:
                mark="O"
                
        if full_board_check(board1):
            print("Draw!!!")
            break
       
        if mark=="O":
            
            os.system('cls')
            display_board(board1)
            print(mark+"'s Turn")
            #print(game_on)
            position=player_choice(board1)
            place_marker(board1, mark, position)
            if win_check(board1, mark)==True:
                os.system('cls')
                display_board(board1)
                
                print("O Won!!")
                break
            else:
                mark="X"
                
        if full_board_check(board1):
            
            os.system('cls')
            display_board(board1)
            
            print("Draw!!!")
            break
        
           
        
       
    if not replay():
        break