import random

print('Welcome to the game. Lets begin!')
print('--------------------------------')

words = ['start', 'hangman', 'college']

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


    def update(self, index, letter):
        for number in index:
            self.display[number] = letter


    def check_guess(self, guess):
        if guess in self.word:
            index = self.get_word(guess)
            self.update(index, guess)


    def check_win(self):
        display = "".join(self.display)
        word = self.word
        if display == word:
            print('You won the game!!!!!')
            return True


def run():
    word = game() #Takes game class and creates run object
    while True:
        guess = input("Choose a letter: ")
        word.check_guess(guess) #Check guesses
        word.show() #Show results
        word.guesses +=1 #Add one
        if word.check_win():
            print(f'Completed in {word.guesses} guesses')
            break


def gameloop():
    while True:
        response = input('Do you want to play Hangman? ' )
        if response == 'no':
            break
        run()

gameloop()