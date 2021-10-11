#!/usr/bin/env python

import random

import brain_games.games.cli


def gcd(a, b):
    remainder_one = a
    remainder_two = b
    if a > b:
        while remainder_one != 0 and remainder_two != 0:
            remainder_one %= remainder_two
            if remainder_one:
                remainder_two %= remainder_one

        return max(remainder_one, remainder_two)

    else:
        while remainder_one != 0 and remainder_two != 0:
            remainder_two %= remainder_one
            if remainder_two:
                remainder_one %= remainder_two

        return max(remainder_one, remainder_two)


def game_gcd():
    name = brain_games.games.cli.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    counter = 0
    while counter < 3:
        number_one = random.randint(1, 1000)
        number_two = random.randint(1, 1000)
        result = str(gcd(number_one, number_two))
        print('Question: ', number_one, number_two)
        answer = input('Your answer: ')
        if answer == result:
            counter += 1
            print('Correct!')
        else:
            counter += 4
            print(f"'{answer}' is wrong answer ;(.", end = '')
            print(f"Correct answer was '{result}'")

    if counter == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


def main():
    game_gcd()


if __name__ == '__main__':
    main()
