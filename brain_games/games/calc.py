from random import randint

from brain_games.welcome_user import welcome_user


def brain_calc():
    name = welcome_user()
    operator_list = ['+', '-', '*']
    print('What is the result of the expression?')
    i = 0
    while i != 3: 
        first_item = randint(0, 10)
        second_item = randint(0, 10)
        operator = operator_list[randint(0, 2)]
        print(f'Question {first_item}{operator}{second_item}')
        if operator == '+': 
            result = first_item + second_item
        if operator == '-':
            result = first_item - second_item
        if operator == '*':
            result = first_item * second_item
        print('Your answer ', end='')
        answer = int(input())
        if result == answer: 
            print('Correct!')
            i += 1
        else: 
            return print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.\nLet's try again, {name}!")
    return print(f'Congratulations, {name}!')