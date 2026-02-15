from brain_games.welcome_user import welcome_user
from random import randint

def brain_gcd(): 
    name = welcome_user() 
    print ('Find the greatest common divisor of given numbers.')
    i = 0 
    while i!= 3: 
        num1 = randint(1,10)
        num2 = randint(1,10)
        print(f'Question: {num1}, {num2}')
        print('Your answer ', end ='')
        answer = (int(input()))

        while num2 != 0: 
            num1, num2 = num2, num1%num2
        if num1 == answer:
            print ('Correct!')
            i += 1 
        else: 
            return print (f"'{answer}' is wrong answer ;(. Correct answer was '{num1}'. \nLet's try again, {name}!")
    print('You win!')   