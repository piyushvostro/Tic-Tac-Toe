def display(board):
    print('   '+'|'+'     '+'|')
    print(board[7]+'  '+'|'+'  '+board[8]+'  '+'|'+'  '+board[9])
    print('   '+'|'+'     '+'|')
    print(board[4]+'  '+'|'+'  '+board[5]+'  '+'|'+'  '+board[6])
    print('   '+'|'+'     '+'|')
    print(board[1]+'  '+'|'+'  '+board[2]+'  '+'|'+'  '+board[3])
    print('   '+'|'+'     '+'|')

def player_input():
    marker=''
    while marker!='X' and marker!='O':
        marker=input('PLAYER 1, CHOOSE SX or O: ').upper()
    player1=marker
    if player1=='X':
        player2='O'
    else:
        player2='X'
    return(player1,player2)

def place_marker(board,marker,position):
    board[position]=marker

def check_winner(board,mark):
    return((board[1]==board[2]==board[3]==mark) or #row checking
    (board[4]==board[5]==board[6]==mark) or #row checking
    (board[7]==board[8]==board[9]==mark) or #row checking
    (board[1]==board[4]==board[5]==mark) or #column checking
    (board[2]==board[5]==board[8]==mark) or #column checking
    (board[3]==board[6]==board[9]==mark) or #column checking
    (board[1]==board[5]==board[9]==mark) or #diagonal ckecking
    (board[3]==board[5]==board[7]==mark)) #diagonal ckecking

def space_check(board, position):
    
    return board[position] == ' '


import random
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('CHOOSE YOUR NEXT POSITION: (1-9) '))
        
    return position

def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
print('\n')
print('----------------------------------------------------')
print('WELCOME TO TIC TAC TOE GAME                  -piyush')
print('----------------------------------------------------')
print('\n')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' WILL GO FIRST')
    
    play_game = input('ARE YOU READY TO PLAY, YES OR NO')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if check_winner(theBoard, player1_marker):
                display(theBoard)
                print('CONGO!! YOU WON THE GAME!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display(theBoard)
                    print('!!!!!DRAW!!!!!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if check_winner(theBoard, player2_marker):
                display(theBoard)
                print('PLAYER 2 HAS WON!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display(theBoard)
                    print('!!!!!DRAW!!!!!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break