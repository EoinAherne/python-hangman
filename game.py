import random

print('Welcome to the game. Lets begin!')
print('--------------------------------')

words = [project, start, hangman, college, game, computer, application, hardware, portfolio, course]

class game:
    def __init__(self):
        self.word = random.choice(words)
        self.display = ['_' for letter in self.word]
        self.guesses = 0