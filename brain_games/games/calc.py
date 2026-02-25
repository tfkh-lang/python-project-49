import operator as op
from random import randint
from typing import Literal

QUESTION = 'What is the result of the expression?'


def apply_operator(
    num1: int,
    num2: int,
    operator: Literal['*', '+', '-']
) -> int:
    match operator:
        case '+':
            action = op.add
        case '-':
            action = op.sub
        case '*':
            action = op.mul
        case _:
            raise ValueError(f'Unexpected operator {operator}')
    return action(num1, num2)


def get_question_and_answer() -> tuple[str, str]:
    operator_list = ['+', '-', '*']
    min_value = 0
    max_value = 10
    first_term = randint(min_value, max_value)
    second_term = randint(min_value, max_value)
    operator = operator_list[randint(0, len(operator_list) - 1)]
    question = f'{first_term} {operator} {second_term}'
    answer = apply_operator(first_term, second_term, operator)
    return question, str(answer)