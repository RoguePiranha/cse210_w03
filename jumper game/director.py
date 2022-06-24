from terminal_service import terminal_service
from animation import animation
from word_list import word_list

class director:
    # The director class is the main class of the program.
    # It contains the main function.
    # It contains the game loop.
    def __init__(self):
        self._terminal_service = terminal_service()
        self._animation = animation()
        self._word_list = word_list()
    
    def start_game(self):
        # The start_game function is the main function of the program.
        # It contains the game loop.
        

        visual_word = ['_']
        guess_word = self._word_list.random_word()
        visual_word = self._word_list.blank_word(guess_word)
        parachute = self._animation.create_parachute_line()

        while '_' in visual_word:
            self._terminal_service.word_line(visual_word)

            self._animation.print_parachute_line(parachute)
            user_guess = self._terminal_service.get_input()

            if user_guess in guess_word:
                visual_word = self._word_list.reveal_letter(guess_word, user_guess)
                print()

            elif user_guess not in guess_word:
                # remove the top parachute line in the list
                parachute.pop(0)

            if '_' not in visual_word:
                print(f"{guess_word}\n")
                print("You win!")

            if len(parachute) == 5:
                parachute[0] = '    x    '
                self._animation.print_parachute_line(parachute)
                print("You lose!")
                print("The word was: " + guess_word)
                break
