from random import randint

QUESTION = 'What is the result of the expression?'


def get_question_and_answer() -> tuple [str, str]:
    operator_list = ['+', '-', '*']
    min_value = 0
    max_value = 10
    first_item = randint(min_value, max_value)
    second_item = randint(min_value, max_value)
    operator = operator_list[randint(0, len(operator_list)-1)]
    question = f'Question: {first_item} {operator} {second_item}'
    if operator == '+': 
        result = first_item + second_item
    if operator == '-':
        result = first_item - second_item
    if operator == '*':
        result = first_item * second_item
    return question, str(result)