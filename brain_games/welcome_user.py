import prompt 

def welcome_user(): 
    print (f'Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name)
    return name