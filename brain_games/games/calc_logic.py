#!/usr/bin/env python

import random

import brain_games.games.cli


def calculate():
    name = brain_games.games.cli.welcome_user()
    print('What is the result of the expression?')
    operators = ['+', '-', '*']
    counter = 0
    while counter < 3:
        number_one = random.randint(1, 100)
        number_two = random.randint(1, 100)
        operator = random.choice(operators)
        expression = str(f'{number_one} {operator} {number_two}')
        print(f'Question: {expression}')
        answer = input('Your answer: ')
        if operator == '+':
            result = str(number_one + number_two)

            if answer == result:
                counter += 1
                print('Correct!')
            else:
                counter += 4
                print(f"'{answer}' is wrong answer ;(.", end = '')
                print(f"Correct answer was '{result}'")

        elif operator == '-':
            result = str(number_one - number_two)

            if answer == result:
                counter += 1
                print('Correct!')
            else:
                counter += 4
                print(f"'{answer}' is wrong answer ;(.", end = '')
                print(f"Correct answer was '{result}'")

        elif operator == '*':
            result = str(number_one * number_two)

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
    calculate()


if __name__ == '__main__':
    main()
