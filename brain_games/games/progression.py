from random import randint


QUESTION = 'What number is missing in the progression?'


def get_progression(start: int, length: int, step: int) -> list[int]:
    progression = []
    for i in range(length):
        current_element = start + i * step
        progression.append(current_element)
    return progression


def get_question_and_answer() -> tuple[str, str]:
    start = randint(1, 1000)
    step = randint(1, 10)
    length = randint(5, 10)
    progression = get_progression(start, length, step)
    hidden_index = randint(0, len(progression) - 1)
    answer = progression[hidden_index]
    progression[hidden_index] = '..'
    progression = ' '.join(map(str, progression))
    question = progression
    return question, str(answer)