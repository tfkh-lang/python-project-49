from random import randint

QUESTION = 'What is the result of the expression?'


def get_answer_of_expression(
    first_term: int, 
    second_term: int, 
    operator: 'str') -> int:
    if operator == '+': 
        answer = first_term + second_term
    if operator == '-':
        answer = first_term - second_term
    if operator == '*':
        answer = first_term * second_term 
    return answer 


def get_question_and_answer() -> tuple[str, str]:
    operator_list = ['+', '-', '*']
    min_value = 0
    max_value = 10
    first_term = randint(min_value, max_value)
    second_term = randint(min_value, max_value)
    operator = operator_list[randint(0, len(operator_list) - 1)]
    question = f'{first_term} {operator} {second_term}'
    answer = get_answer_of_expression(first_term, second_term, operator)
    return question, str(answer)