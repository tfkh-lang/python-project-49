from random import randint


question = 'What number is missing in the progression?'


def sequence() -> list:
    progression = []
    start = randint(1, 1000)
    step = randint(1, 10)
    long = randint(5, 10)
    for i in range(long):
        currentElement = start + i * step
        progression.append(currentElement)

    return progression


def hide_element_in_sequance() -> list: 
    progression = sequence()
    len_list = len(progression)
    hide_index = randint(0, len_list - 1)
    hide_element = progression[hide_index]
    progression[hide_index] = '..'
    progression_str = ' '.join(map(str, progression))
    return progression_str, hide_element


def game() -> str: 
    progression, element = hide_element_in_sequance()
    question = f'Question: {progression}'
    return str(element), question



