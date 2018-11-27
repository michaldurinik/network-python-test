class Tile:

    def __init__(self, letter="", value=0):
        self.letter = letter
        self.value = value

        # Tile class will hold numerical value of the tile
        # and it's actual corresponding letter.

    def check_value(self):
        # It will return numerical value of tile when requested.
        return self.value

    def check_letter(self):
        # It will return letter of tile when requested.
        return self.letter
