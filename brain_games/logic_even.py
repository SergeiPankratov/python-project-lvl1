#!/usr/bin/env python

import random

import prompt


def even_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < 3:
        number = random.randint(0, 1000)
        test_number = number % 2
        print(f'Question: {number}')
        answer = input('Your answer: ')
        if test_number == 0 and answer == 'yes':
            counter += 1
            print('Correct!')

        elif test_number != 0 and answer == 'no':
            counter += 1
            print('Correct!')

        else:
            counter += 4
            if answer == 'yes':
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                print(f"Let's try again, {name}")
            else:
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                print(f"Let's try again, {name}")
    if counter == 3:
        print(f'Congratulations, {name}!')


def main():
    even_game()


if __name__ == '__main__':
    main()
