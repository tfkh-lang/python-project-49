from random import randint

question = 'What is the result of the expression?'


def game() -> str:
    operator_list = ['+', '-', '*']
    first_item = randint(0, 10)
    second_item = randint(0, 10)
    operator = operator_list[randint(0, 2)]
    question = f'Question: {first_item} {operator} {second_item}'
    if operator == '+': 
        result = first_item + second_item
    if operator == '-':
        result = first_item - second_item
    if operator == '*':
        result = first_item * second_item
    return str(result), question

