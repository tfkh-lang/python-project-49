import types

from brain_games.welcome_user import welcome_user

GAME_ROUNDS_COUNT = 3 


def run(game: types.ModuleType) -> None:
    name = welcome_user()
    print(game.QUESTION)
    for _ in range(GAME_ROUNDS_COUNT):
        question, result = game.get_question_and_answer()
        print(question)
        print('Your answer: ', end='')
        answer = input()
        if result == answer: 
            print('Correct!')
        else: 
            print(f"'{answer}' is wrong answer. Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')