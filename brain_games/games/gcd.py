from random import randint


QUESTION = 'Find the greatest common divisor of given numbers.'

def get_gsd() -> int: 
    min_value, max_value = 1, 10
    random_number_1 = randint(min_value, max_value)
    random_number_2 = randint(min_value, max_value)
    number_1 = random_number_1
    number_2 = random_number_2
    while number_2 != 0: 
        number_1, number_2 = number_2, number_1 % number_2
    return number_1, random_number_1, random_number_2

def get_question_and_answer() -> tuple [str, str]: 
    answer, num1, num2 = get_gsd()
    question = f'Question: {num1} {num2}'
    return question, str(answer)
