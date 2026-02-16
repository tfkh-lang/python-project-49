from random import randint

from brain_games.welcome_user import welcome_user


def sequence() -> list:
    progression = []

    start = randint(1, 1000)
    step = randint(1, 10)
    long = randint(5, 10)

    for i in range(long):
        currentElement = start + i * step
        progression.append(currentElement)

    return progression


def hide_element_in_sequance(): 
    progression = sequence()
    len_list = len(progression)
    hide_index = randint(0, len_list - 1)
    hide_element = progression[hide_index]
    progression[hide_index] = '..'
    progression_str = ' '.join(map(str, progression))
    return progression_str, hide_element

def game_progression(): 
    name = welcome_user()
    print('What number is missing in the progression?') 
    i = 0
    while i != 3:
        progression, element = hide_element_in_sequance()
        print(f'Question {progression}')
        print('Your answer ', end='')
        answer = (int(input()))
        if answer == element: 
            print('Correct!')
            i += 1
        else: 
            return print(f"'{answer}' is wrong answer ;(. Correct answer was '{element}'. \nLet's try again, {name}!")
    print('You win!')    


