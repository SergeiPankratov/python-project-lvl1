#!/usr/bin/env python

import random

import brain_games.games.cli


def is_prime(n):
    d = 2
    while n % d != 0:
        d += 1
    return n == d


def is_prime_game():
    name = brain_games.games.cli.welcome_user()
    print('Answer "yes" if given number is prime. ', end = '')
    print('Otherwise answer "no".')
    counter = 0
    while counter < 3:
        random_number = random.randint(1, 100)
        print('Question: {}'.format(random_number))
        answer = input('Your answer: ')
        result = is_prime(random_number)
        if answer == 'yes':
            if result:
                counter += 1
                print('Correct!')
            else:
                counter += 4
                print(f"'{answer}' is wrong answer ;(. ", end = '')
                print("Correct answer was 'no'")
        else:
            if result:
                counter += 4
                print(f"'{answer}' is wrong answer ;(. ", end = '')
                print("Correct answer was 'yes'")

            else:
                counter += 1
                print('Correct!')

    if counter == 3:
        print(f'Congratulations, {name}!')

    else:
        print(f"Let's try again, {name}!")


def main():
    is_prime_game()


if __name__ == '__main__':
    main()
