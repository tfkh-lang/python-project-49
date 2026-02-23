from random import randint

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num: int) -> bool:
    return num % 2 == 0


def get_question_and_answer() -> tuple[str, str]:
    min_value, max_value = 1, 1000
    number = randint(min_value, max_value) 
    question = f'Question: {number}'
    if is_even(number):
        return question, 'yes'
    else: 
        return question, 'no'