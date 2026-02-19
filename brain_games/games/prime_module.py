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


def prime(): 
    num = randint(0, 100)
    print('Qyestion: ', num)
    if is_prime(num): 
        return 'yes'
    else: 
        return 'no'


function = prime