from brain_games.welcome_user import welcome_user
from random import randint

def is_prime(num: int) -> bool:
    if num <= 1: 
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    else:
            return True

def prime(): 
    name = welcome_user()
    print ('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i != 3:
        num = randint (0, 100)
        print ('Qyestion: ', num)
        print('Your answer ', end ='')
        answer = input()
        
        if is_prime (num) and answer == 'yes': 
             print ('Correct!') 
             i += 1
        elif is_prime (num) and answer == 'no':
             return (print (f"'{answer}' is wrong answer ;(.\nLet's try again, {name}!"))
        elif not is_prime (num) and answer == 'no':
            print ('Correct!') 
            i += 1
        else: 
             return (print (f"'{answer}' is wrong answer ;(.\nLet's try again, {name}!"))
    print('You win!')   

