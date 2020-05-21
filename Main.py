import random

dict = {'Player1': '', 'Player2': ''}
board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
game_on = True
keep_playing = True

## Print Board ##
def print_board(a_board):
    print(' {} | {} | {}'.format(a_board[1], a_board[2], a_board[3]))
    print('---|---|---')
    print(' {} | {} | {}'.format(a_board[4], a_board[5], a_board[6]))
    print('---|---|---')
    print(' {} | {} | {}'.format(a_board[7], a_board[8], a_board[9]))

## Return tuple with symbols in (player1, player2) form ##
def id_players():
    symbol = ''

    while symbol.upper() != 'X' and symbol.upper() != 'O':
        symbol = input("Player1 chooses symbol (X or O) to play: ").upper().strip()

    if symbol == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'

## Gets position where to place player's id and it validates it before it places it ##
def get_move(player_id):
    number = 0
    global board

    while True:
        try:
            if dict['Player1'] == player_id:
                number = int(input('\nPlayer1 select a number in you keypad for your next move. range(1...9) '))
            else:
                number = int(input('\nPlayer2 select a number in you keypad for your next move. range(1...9) '))
        except ValueError:
            print('Wrong input. Try again!\n')
            print_board(board)
            continue

        if board[number] != 'X' and board[number] != 'O' and number != 0:
            board[number] = player_id
            break
        else:
            print('This space is not available. Try again!\n')
            print_board(board)
            continue

## Randomly selects who plays firs#
def plays_first():
    if random.randint(0,1) == 0:
        return 'Player1'
    else:
        return 'Player2'

## Checks for same player_id completion to win horizontally, vertically and diagonally ##
def got_winner(board, player_id):
    if (board[1] == board[2] == board[3] == player_id) or \
        (board[4] == board[5] == board[6] == player_id) or \
        (board[7] == board[8] == board[9] == player_id) or \
        (board[1] == board[4] == board[7] == player_id) or \
        (board[2] == board[5] == board[8] == player_id) or \
        (board[3] == board[6] == board[9] == player_id) or \
        (board[3] == board[5] == board[7] == player_id) or \
        (board[1] == board[5] == board[9] == player_id):
        return True
    else:
        return False


## Check if all spaces have been filled ##
def full_board():
    for i in range(1,10):
        if board[i] != 'X' and board[i] != 'O':
            return False
    return True


## Game Logic ##
while keep_playing:
    board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    print('\n\nWelcome to my Tic Tac Toe!')
    print('##########################')
    print_board(board)
    print('##########################')
    dict['Player1'], dict['Player2'] = id_players()
    print(f"Player1's ID is {dict['Player1']} and Player2's ID is {dict['Player2']}.")
    if plays_first() == 'Player1':
        first_player = 'Player1'
        second_player = 'Player2'
    else:
        first_player = 'Player2'
        second_player = 'Player1'
    print(f"The first move will be made by {first_player}. ")

    while game_on:
        #First Player's turn
        get_move(dict[first_player])
        print_board(board)
        if got_winner(board, dict[first_player]):
            print(f"\nThe winner is {first_player}.")
            play_again = input("Do you want to play again [Y/N]").upper().strip()
            game_on = False
            break
        elif not got_winner(board, dict[first_player]) and full_board():
            print("\nTIE GAME!")
            play_again = input("Do you want to play again [Y/N]").upper().strip()
            game_on = False
            break

        #Second Player's turn
        get_move(dict[second_player])
        print_board(board)
        if got_winner(board, dict[second_player]):
            print(f"\nThe winner is {second_player}")
            play_again = input("Do you want to play again [Y/N]").upper().strip()
            game_on = False
        elif not got_winner(board, dict[second_player]) and full_board():
            print("\nTIE GAME!")
            play_again = input("Do you want to play again [Y/N]").upper().strip()
            game_on = False

    if play_again != 'Y':
        keep_playing = False
print('#################################')
print("Thank you for playing.\nGood Bye.")
print('#################################')
