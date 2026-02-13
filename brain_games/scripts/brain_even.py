from random import randint

import prompt 


def welcome_user(): 
    name = prompt.string('May I have your name? ')
    print('Hello,', name)
    return name

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
        answer = str(input())

        if numb % 2 == 0 and answer == y:
            print('Correct!')
            i += 1
        elif numb % 2 != 0 and answer == n:
            print('Correct!')
            i += 1
        elif numb % 2 == 0 and answer == n:
            return print(f"'{n}' is wrong answer ;(. Correct answer was '{y}'.\nLet's try again, {name}!!")
        elif numb % 2 != 0 and answer == y:
            return print(f"'{y}' is wrong answer ;(. Correct answer was '{n}'.\nLet's try again, {name}!!")


def main():
    brain_even()


if __name__ == "__main__":
    main()


