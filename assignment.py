import random


def get_user_guess():
    user_guess = input('Guess a number between 1 and 10: ')
    try:
        return int(user_guess)
    except:
        print('Please input a number')
        return get_user_guess()


def run_guess_loop(guess_limit):
    correct_number = random.randint(1, 10)
    # For debug purposes
    # print(correct_number)
    guess_count = 0
    you_won = False

    while guess_count < guess_limit:

        if get_user_guess() == correct_number:
            you_won = True
            print('You guessed the right number, You win!')
            break
        else:
            you_won = False
            print('Wrong Guess!')
            guess_count += 1

    if not you_won:
        print(f'The right number is {correct_number}')
        print('You Lose!')


def run_game(guess_limit):
    print('This is a game of luck. Test your luck!')

    should_run = True

    while should_run:
        run_guess_loop(guess_limit)
        should_run = re_run()


def re_run():
    should_rerun = input('Do you want to try again? Enter yes or no: ')
    if should_rerun.lower() == 'yes':
        return True
    elif should_rerun.lower() == 'no':
        print('Thank you for playing')
        return False
    else:
        print('Please enter yes or no')
        return re_run()


run_game(3)