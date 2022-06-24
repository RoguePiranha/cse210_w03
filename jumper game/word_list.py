from words_bank import word_bank
from random import randint

class word_list:
    # Contains a list of words to be used in the game.
    # The list is randomly chosen from.
    
    def __init__(self):
        # define variables to be used throughout the program

        self.guess_word = ""
        self.blank_list = []
        self._word_list = word_bank()

    def random_word(self):
        # randomly choose a word from the list
        # return the word
        words_list = self._word_list.list_of_words()
        self.guess_word = words_list[randint(0, len(words_list) - 1)]
        return self.guess_word

    def blank_word(self, guess_word):
        # return a blank word
        for i in range(len(guess_word)):
            self.blank_list.append("_")

        return self.blank_list

    def reveal_letter(self, guess_word, user_guess):
        # reveal the letter in the word
        for i in range(len(guess_word)):
            if guess_word[i] == user_guess:
                self.blank_list[i] = user_guess

        return self.blank_list
