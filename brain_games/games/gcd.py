from random import randint


QUESTION = 'Find the greatest common divisor of given numbers.'


def get_gsd(number_1, number_2) -> int: 
    while number_2 != 0: 
        number_1, number_2 = number_2, number_1 % number_2
    return number_1 


def get_question_and_answer() -> tuple[str, str]:
    min_value, max_value = 1, 10
    number_1 = randint(min_value, max_value)
    number_2 = randint(min_value, max_value)
    answer = get_gsd(number_1, number_2)
    question = f'Question: {number_1} {number_2}'
    return question, str(answer)