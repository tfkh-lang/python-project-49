from brain_games.welcome_user import welcome_user


ALL_ROUNDS_OF_GAME = 3 

def run(game: types.ModuleType):
    name = welcome_user()
    print (game.question)
    r = 0
    while r != ALL_ROUNDS_OF_GAME: 
        result = game.function()
        print(f'Your answer ', end='')
        answer =  input()
        if str(result) == answer: 
            print(f'Correct!')
            r += 1
        else: 
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')