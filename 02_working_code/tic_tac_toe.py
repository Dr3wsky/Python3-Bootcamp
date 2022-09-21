# Import Modules
import os
from random import randint

# Define game functions
def display_board(board_state):
    print('\n')
    print(f'  {board_state[0]}  |  {board_state[1]}  |  {board_state[2]} ')
    print(f'-----|-----|-----')
    print(f'  {board_state[3]}  |  {board_state[4]}  |  {board_state[5]} ')
    print(f'-----|-----|-----')
    print(f'  {board_state[6]}  |  {board_state[7]}  |  {board_state[8]} ')
    print('\n')


# Initialize game
def initialize():
    marker = ' '
    print(f'Player {p_count} starts')
    marker = input('Choose your marker: X or O: ').upper()
    while not (marker == 'X' or marker == 'O'):
        marker = input(f'Invalid selection. Player {p_count} please choose X or O as your marker: ').upper()
    if ((marker == 'X' and p_count == 1) or (marker == 'O' and p_count == 2)):
        return {'Player 1': 'X', 'Player 2': 'O'}
    else:
        return {'Player 1': 'O', 'Player 2': 'X'}


# Place marker on board
def place_marker(board_state, p_dict, p_count, place):
    board_state[place] = p_dict['Player ' + str(p_count)]
    display_board(board_state)
    return board_state


# Check if player won
def check_win(board_state, p_dict, p_count):
    mark = p_dict['Player ' + str(p_count)]
    return ((board_state[0] == mark and board_state[1] == mark and board_state[2] == mark) or  # across top check
            (board_state[3] == mark and board_state[4] == mark and board_state[5] == mark) or  # across middle check
            (board_state[6] == mark and board_state[7] == mark and board_state[8] == mark) or  # across bottom check
            (board_state[0] == mark and board_state[3] == mark and board_state[6] == mark) or  # down left check
            (board_state[1] == mark and board_state[4] == mark and board_state[7] == mark) or  # down middle check
            (board_state[2] == mark and board_state[5] == mark and board_state[8] == mark) or  # down middle check
            (board_state[0] == mark and board_state[4] == mark and board_state[8] == mark) or  # TL diag check
            (board_state[2] == mark and board_state[4] == mark and board_state[6] == mark))  # BL diag check


# Check if position choice is open
def check_free(board_state, place):
    return board_state[place] == ' '


# Check if board is full
def check_full(board_state):
    for num in range(0, len(board_state)):
        if check_free(board_state, num):
            return False
    return True


# Prompt player choice and save response for other inputs
def player_choice(p_count, p_dict, board_state):
    place = input(f"Player {p_count}'s turn - You are {p_dict['Player ' + str(p_count)]}. Choose your next placement (1-9): ")
    while place not in ['1', '2', '3', '5', '6','7', '8', '9']:
        place = input(f"Invalid selection - Playe {p_count} choose your next placement (1-9): ")
    place = int(place)-1
    while check_free(board_state, place) == False:
        place = input('Invalid selection, choose an open spot on the board: [1-9]')
        place = int(place) - 1
        check_free(board_state, place)
    return place


# Prompt Replay
def replay():
    if input('Do you want to play again? Enter Yes or No: ').lower().startswith('y') == True:
        return 18
    else:
        return 21


# Reset game for a replay
def reset_game():
    p_count = randint(1, 2)
    for num in range(0, len(board_state)):
        board_state[num] = ' '
    return board_state, p_count


# ---------------------------------------------------------------------------------------- #
## GAME LOGIC ##
# ---------------------------------------------------------------------------------------- #



# Initialize vars
p_count = randint(1, 2)
board_state = [1, 2, 3, 4, 5, 6, 7, 8, 9]
game_on = 0
print('Welcome to tic-tac-toe')

# Initialize player options, board and rules
p_dict = initialize()
print('The game is simple, use the numbers to select your play position corresponding to the grid below:')
display_board(board_state)
print('Good Luck!')

# Clear board for play 
for num in range(0, len(board_state)):
    board_state[num] = ' '

while game_on <= 19:

    if game_on == 19:  # Reset the board for a replay
        p_count = randint(1, 2)
        for num in range(0, len(board_state)):
            board_state[num] = ' '
        initialize()
        display_board(board_state)
        game_on = 0
        os.system('cls')

    # Prompt selection
    place = player_choice(p_count, p_dict, board_state)

    # Place marker and check for win or draw
    place_marker(board_state, p_dict, p_count, place)
    if check_win(board_state, p_dict, p_count) == True:
        print(f"GAME OVER - PLAYER {p_count} WINS !!!")
        game_on = replay()
    elif check_full(board_state) == True:
        print("CAT'S GAME - IT'S A DRAW")
        game_on = replay()

    # Clear screen and change turn\

    if p_count == 1:
        p_count += 1
    else:
        p_count = 1
    game_on += 1
    os.system('cls')

print('Thanks for playing :)')

## Debug status:
# Everything is working and logic checks out. 
# Need to add a screen clear function to claer the screen and it doesn't scroll every time
