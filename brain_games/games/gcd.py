from random import randint


question = 'Find the greatest common divisor of given numbers.'


def game() -> str: 
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    question = f'Question: {num1} {num2}'
    while num2 != 0: 
        num1, num2 = num2, num1 % num2
    return str(num1), question
