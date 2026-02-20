from random import randint

question = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num: int) -> bool:
    return num % 2 == 0


def brain_even():
    numb = randint(1, 1000) 
    print(f'Question: {numb}')
    if is_even(numb):
        return 'yes'
    else: 
        return 'no'
    
    
game = brain_even