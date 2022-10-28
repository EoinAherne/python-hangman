import random

print('Welcome to the game. Lets begin!')
print('--------------------------------')

words = [start, hangman, college, game, computer, application, hardware, portfolio, course]

class game:
    def __init__(self):
        self.word = random.choice(words)
        self.display = ['_' for letter in self.word]
        self.guesses = 0

    def show(self):
        display = ' '.join(self.display)
        print(f'The answer is: {display}')