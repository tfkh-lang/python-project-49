from random import randint

question = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num: int) -> bool:
    return num % 2 == 0


def game() -> str:
    numb = randint(1, 1000) 
    question = f'Question: {numb}'
    if is_even(numb):
        return 'yes', question
    else: 
        return 'no', question
