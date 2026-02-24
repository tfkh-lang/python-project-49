import types

from brain_games.welcome_user import welcome_user

GAME_ROUNDS_COUNT = 3 


def run(game: types.ModuleType) -> None:
    name = welcome_user()
    print(game.QUESTION)
    for _ in range(GAME_ROUNDS_COUNT):
        question, answer = game.get_question_and_answer()
        print(question)
        user_answer = input('Your answer: ')
        if answer == user_answer: 
            print('Correct!')
        else: 
            wrong_line_part_1 = f"'{user_answer}' is wrong answer."
            wrong_line_part_2 = f" Correct answer was '{answer}'."
            print(wrong_line_part_1 + wrong_line_part_2)
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')