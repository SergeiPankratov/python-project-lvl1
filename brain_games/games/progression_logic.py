#!/usr/bin/env python

import random

import brain_games.games.cli


def progression():
    start = random.randint(1, 1000)
    amount_of_numbers = random.randint(5, 10)
    step = random.randint(1, 100)
    sequence = []
    while amount_of_numbers > 0:
        sequence.append(start)
        start += step
        amount_of_numbers -= 1

    question = ''
    random_number = random.choice(sequence)
    for i in sequence:
        if i == random_number:
            question += '{} '.format('..')

        else:
            question += '{} '.format(i)
    question = question[: len(question) - 1]
    return (question, random_number)


def game_progression():
    name = brain_games.games.cli.welcome_user()
    counter = 0
    while counter < 3:
        (question, random_number) = progression()
        print(f'Question: {question}')
        answer = input('Your answer: ')
        if answer == str(random_number):
            counter += 1
            print('Correct!')

        else:
            counter += 4
            print(f"'{answer}' is wrong answer ;(.", end = '')
            print(f"Correct answer was '{random_number}'")

    if counter == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


def main():
    game_progression()


if __name__ == '__main__':
    main()
