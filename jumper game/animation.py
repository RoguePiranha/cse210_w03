class animation:
    # Need comments
    def __init__(self):
        # define variables to be used throughout the program

        self._parachute_line = ""
        self._parachute = []

    def create_parachute_line(self):
        # create the parachute line
        
        self._parachute = [
            "  _____  ",
            " /_____\ ",
            " \     / ",
            "  \   /  ",
            "   \ /   ",
            "    O    ",
            "   /|\   ",
            "   / \   ",
            "         ",
            " ^^^^^^^ "
        ]
        print()

        return self._parachute

    def print_parachute_line(self, parachute):
        # print the parachute line
        
        for i in range(0, len(parachute)):
            print(parachute[i], flush=True)

        return parachute