import types

from brain_games.welcome_user import welcome_user

GAME_ROUNDS_COUNT = 3 


def run(game: types.ModuleType) -> None:
    name = welcome_user()
    print(game.QUESTION)
    for _ in range(GAME_ROUNDS_COUNT):
        question, answer = game.get_question_and_answer()
        print(question)
        user_a = input('Your answer: ')
        if answer == user_a: 
            print('Correct!')
        else: 
            print(f"'{user_a}' is wrong answer. Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')