from random import randint
from brain_games.welcome_user import welcome_user
import prompt 

def is_even(num:int) -> bool:
    return num%2 == 0


def brain_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0 
    while i != 3: 
        numb = randint(1, 1000) 
        y = 'yes'
        n = 'no'
        print('Question: ', numb)
        print('Your answer ', end='')
        answer = input()
        if is_even(numb) and answer == y:
            print('Correct!')
            i += 1
        elif not is_even(numb) and answer == n:
            print('Correct!')
            i += 1
        elif is_even(numb) and answer == n:
            return print(f"'{n}' is wrong answer ;(. Correct answer was '{y}'.\nLet's try again, {name}!!")
        elif not is_even(numb) and answer == y:
            return print(f"'{y}' is wrong answer ;(. Correct answer was '{n}'.\nLet's try again, {name}!!")
    print ('You win!')