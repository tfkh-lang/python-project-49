from random import randint


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num: int) -> bool:
    if num <= 1: 
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_question_and_answer() -> tuple[int, str]: 
    min_value, max_value = 0, 100
    num = randint(min_value, max_value)
    question = num
    return question, 'yes' if is_prime(num) else 'no'