import random

print('Welcome to the game. Lets begin!')
print('--------------------------------')

words = ['start', 'hangman', 'college', 'game', 'computer', 'application', 'hardware', 'portfolio', 'course']

class game:
    def __init__(self):
        self.word = random.choice(words)
        self.display = ['_' for letter in self.word]
        self.guesses = 0

    def show(self):
        display = ' '.join(self.display)
        print(f'The answer is: {display}')

    def get_word(self, guess):
        word_location = []

        for index, char in enumerate(list(self.word)):
            if char == guess:
                word_location.append(index)
        return word_location
