from Ipython.display import clear_output
def player_board(board):
	clear_output()
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---|---|---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---|---|---')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
def player_input():
	marker = ''

	while not (marker == 'X' or marker == 'O'):
		marker = input('Player 1 please choose a mareker X or O:  ')
	if marker == 'X':
		return ('X' , 'O')

	else:
		return ('O' , 'X')
def place_marker(board,marker,position):
	board[position] = marker 
def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark))
import random
def choose_first():
	if random.randint(0,1) == 0:
		return 'Player1'
	else:
		return 'Player2'
def space_check(board,position):
	return board[position] == ' '
def full_board_check(board):
	for i in range(1,10):
		if space_check() == True:
			return False
	return True
def player_choice(board):
	position = 0
	while position not in range(1,10) or space_check(board,position) == False:
		position = int(input("Please enter a position from the numbers 1 to 9:  "))
	return position
def replay():
	choice = input('Do you want to continue please enter Y or N:   ').upper()
	while choice != Y or choice != N:
		choice = input('Do you want to continue please enter Y or N:   ').upper()
	return choice 



#GAMEPLAY
print("Welcome to TIC TAC TOE")
play_game = ''
while play_game not in ('y', 'n'):
    play_game = input("Ready to play the game? y or n:  ").lower()
    if play_game not in ('y', 'n'):
        print("Please enter 'y' or 'n'.")
if play_game == 'n':
	replay = False
else:
	replay = True
while replay == True:
	game_board = [' ']*10
	Player1_marker , Player2_marker = player_input()
	turn = choose_first()
	print(turn + "will go first")
	while game_on == True:
		if turn == 'Player1':
			player_board(game_board)
			game_position = player_choice(game_board)
			place_marker(game_board,Player1_marker,game_position)
			if win_check(game_board,Player1_marker) == True:
				player_board(game_board)
				print("Player 1 has won the game")
				game_on = False
			else:
				if full_board_check(game_board) == True:
					player_board(game_board)
					print("This match is a tie")
					game_on = False
				else:
					turn = 'Player2' 
		else turn == 'Player2':
			player_board(game_board)
			game_position = player_choice(game_board)
			place_marker(game_board,Player2_marker,game_position)
			if win_check(game_board,Player2_marker) == True:
				player_board(game_board)
				print("Player 2 has won the game")
				game_on = False
			else:
				if full_board_check(game_board) == True:
					player_board(game_board)
					print("This match is a tie")
					game_on = False
				else:
					turn = 'Player1' 
	if replay == False:
		break
replay()

