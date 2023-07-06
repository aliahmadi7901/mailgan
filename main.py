import random
from config import GAME_CHOICES, RULES, scoreboard
from duration import log_time


def get_user_choice():
    user_input = input('please enter your choice (r, p, s): ')
    if user_input not in GAME_CHOICES:
        print('oops!! wrong choice, please try again...')
        return get_user_choice()
    return user_input


def get_system_choice():
    return random.choice(GAME_CHOICES)


def find_winner(user, system):
    match = {user, system}
    if len(match) == 1:
        return None
    else:
        return RULES[tuple(sorted(match))]


def update_scoreboard(result):
    if result['user'] == 3:
        scoreboard['user'] += 1
        msg = 'you win'
    else:
        scoreboard['system'] += 1
        msg = 'you lose'

    print('result all:')
    print('#'*36)
    print('##', f"user:{scoreboard['user']}".ljust(30), '##')
    print('##', f"system:{scoreboard['system']}".ljust(30), '##')
    print('##', f"result of last game: {msg}".ljust(30), '##')
    print('#'*36)


def do_you_want_play_again():
    play_again = input('Do you want to play again? (y/n):')
    if play_again == 'y':
        play()
    elif play_again == 'n':
        print('we hope you enjoy to play.see you later')
    else:
        print('oops!!wrong choice, please try again...')
        return do_you_want_play_again()


def get_hand_of_game():
    user_input = input('how many hands of game?enter a number:')

    try:
        user_number = int(user_input)
        return user_number
    except ValueError:
        print('invalid number!!please try again...(1,2,3,4...)')
        return get_hand_of_game()


def play():

    result = {'user': 0, 'system': 0}
    hand_of_game = get_hand_of_game()
    while result['user'] < hand_of_game and result['system'] < hand_of_game:
        user_choice = get_user_choice()
        system_choice = get_system_choice()
        winner = find_winner(user_choice, system_choice)
        if user_choice == winner:
            msg = 'you win'
            result['user'] += 1
        elif system_choice == winner:
            msg = 'you lose'
            result['system'] += 1
        else:
            msg = 'Draw'

        print(f"user:{user_choice}\tsystem:{system_choice}\tresult:{msg}")
    print('result of this hand:')
    print(result)
    update_scoreboard(result)
    do_you_want_play_again()


@log_time
def information():
    print('welcome to this game.\tautor:ali ahmadi')
    print(
        'this game have a someone rules:\n'
        '1-winner of ( r , p ) is ( p )\n'
        '2-winner of ( p , s ) is ( s )\n3-winner of ( r , s ) is ( r ).'
    )
    print('lets go...')
    play()


if __name__ == '__main__':
    information()
