# Player class
#
# Filename: player.py
# Project: SRUS-HS-Games
# Author: Andres Jarava <200700718@tafe.wa.edu.au>
# Date Created: 16/2/22
# ----------------------------------------------------------------------

class Player:
    """
    Player class
    """

    def __init__(self, uid, name):
        """
        Constructor
        @param uid: player id
        @param name: player name
        """
        self.__id = uid
        self.__name = name

    @property
    def id(self):
        """
        Getter for player id
        @return: player id
        """
        return self.__id

    @property
    def name(self):
        """
        Getter for player name
        @return: player name
        """
        return self.__name

    def __str__(self):
        """
        String representation of player
        @return: string representation of player
        """
        return f"Player: {self.__name} with id: {self.__id}"


# if __name__ == "__main__":
#     player = Player("1", "Andres")
#     print(player)
