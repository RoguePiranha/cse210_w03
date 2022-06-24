from director import director

continue_game = True
while continue_game:
    Director = director()
    Director.start_game()
    print()
    yesorno = input("Do you want to play again? (y/n) ")
    if yesorno == "n":
        continue_game = False
        print("Thanks for playing!")