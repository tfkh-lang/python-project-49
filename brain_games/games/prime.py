from random import randint


question = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num: int) -> bool:
    if num <= 1: 
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True


def game() -> str: 
    num = randint(0, 100)
    question = f'Question: {num}'
    if is_prime(num): 
        return 'yes', question
    else: 
        return 'no', question


