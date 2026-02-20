import types

from brain_games.welcome_user import welcome_user

GAME_ROUNDS_COUNT = 3 


def run(games: types.ModuleType) -> None:
    name = welcome_user()
    print(games.question)
    for round in range(GAME_ROUNDS_COUNT):
        result, question = games.game()
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