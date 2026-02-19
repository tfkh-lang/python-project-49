from random import randint

question = f'Find the greatest common divisor of given numbers.'

def brain_gcd(): 
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    print(f'Question: {num1}, {num2}')
    while num2 != 0: 
        num1, num2 = num2, num1 % num2
    return num1 

function = brain_gcd