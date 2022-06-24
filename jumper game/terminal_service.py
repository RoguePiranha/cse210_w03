class terminal_service:
    # prints interaction within the terminal
    # receives user input

    def get_input(self):
        #  receives user input

        print()
        guess_letter = input("Guess a letter [a-z]: ")
        print()

        return guess_letter

    def word_line(self, visual_word):
        # prints the word line
        # receives user input

        for i in visual_word:
            print(i, end=" ")
        print()
        print()