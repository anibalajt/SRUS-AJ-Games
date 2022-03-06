# Player class
#
# Filename: player.py
# Project: SRUS-HS-Games
# Author: Andres Jarava <200700718@tafe.wa.edu.au>
# Date Created: 16/2/22
# ----------------------------------------------------------------------
from argon2 import PasswordHasher


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

    def add_password(self, password):
        """
        Add password to player
        @param password: plaintext password
        """
        self.__password = PasswordHasher().hash(password)

    def verify_password(self, password):
        """
        Verify password
        @param password: plaintext password
        @return: True if password matches, False otherwise
        """
        try:
            return PasswordHasher().verify(self.__password, password)
        except Exception:
            return False

    def __str__(self):
        """
        String representation of player
        @return: string representation of player
        """
        return f"Player: {self.__name} with id: {self.__id}"


# if __name__ == "__main__":
#     player = Player("1", "Andres")
#     player.add_password("password")
#     print('password ', player.verify_password("password"))
#     print('password ', player.verify_password("wrong_password"))
#     print(player)
#     print(player.id)
#     print(player.name)
