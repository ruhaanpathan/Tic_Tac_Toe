print('\n'*30)
def display_board(board):
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[7]+'|'+board[8]+'|'+board[9])
def player_input():
    marker=''

    while marker !='X' and marker!='O':
        marker = input('player1:choose x or o: ').upper()
    if marker =='X':
        return('X','O')
    else:
        return('O','X')


def place_marker(board,marker,position):
    board[position]=marker
def win_check(board,mark):
    return((board[1]==board[2]==board[3]==mark)or
           (board[4]==board[5]==board[6]==mark)or
           (board[7]==board[8]==board[9]==mark)or
           (board[1]==board[4]==board[7]==mark)or
           (board[2]==board[5]==board[8]==mark)or
           (board[3]==board[6]==board[9]==mark)or
           (board[1]==board[5]==board[9]==mark)or
           (board[3]==board[5]==board[7]==mark))
import random
def choose_first():
    flip=random.randint(0,1)
    if flip==0:
        return'player1'
    else:
        return'player2'
def space_check(board,position):
    return board[position]==' '
def full_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        try:
            position =int(input('choose a position: (1-9)'))
        except Exception:
            print('Please do not enter any letter')
            
        if position is (1,2,3,4,5,6,7,8,9):
            continue
        else:
            print('please select number from 1 to 9 only')
            continue
    return position
def replay():
    choice = input('play again? enter yes or no: ')
    return choice=='yes'

print('welcome to the tic tac toe')

while True:
    the_board=[' ']*10
    player1,player2 = player_input()
    turn = choose_first()
    print(turn + ' will go first')
    play_game = input('ready to play? y or n?')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'player 1':
            display_board(the_board)
            
            position= player_choice(the_board)
            place_marker(the_board,player1,position)
            if win_check(the_board,player1):
                display_board(the_board)
                print('player 1 has won')
                game_on = False
            else:
                if full_check(the_board):
                    display_board(the_board)
                    print('tie')
                    break
                else:
                    turn = 'player 2'
        else:
            turn == 'player 2'
            display_board(the_board)
            
            position= player_choice(the_board)
            place_marker(the_board,player2,position)
            if win_check(the_board,player2):
                display_board(the_board)
                print('player 2 has won')
                game_on = False
            else:
                if full_check(the_board):
                    display_board(the_board)
                    print('tie')
                    break
                else:
                    turn = 'player 1'
    if not replay():
        break
