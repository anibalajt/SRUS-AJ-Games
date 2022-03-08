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
        self.__score = 0

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

    @property
    def score(self):
        """
            Getter for score
            @return: score
            """
        return self.__score

    @score.setter
    def score(self, score):
        """
        Setter for score
        @param score: score
        """
        self.__score = score

    def __str__(self):
        """
        String representation of player
        @return: string representation of player
        """
        return f"Player: {self.__name} with id: {self.__id}"

    def __eq__(self, other):
        """
        Compare players by score
        @param other: other player
        @return: True if players have the same score, False otherwise
        """
        return self.__score == other.__score

    def __ge__(self, other):
        """
        Compare players by score
        @param other: other player
        @return: True if self has a higher score than other, False otherwise
        """
        return self.__score >= other.__score

    def __gt__(self, other):
        """
        Compare players by score
        @param other: other player
        @return: True if self has a higher score than other, False otherwise
        """
        return self.__score > other.__score

    def __le__(self, other):
        """
        Compare players by score
        @param other: other player
        @return: True if self has a lower score than other, False otherwise
        """
        return self.__score <= other.__score

    def __lt__(self, other):
        """
        Compare players by score
        @param other: other player
        @return: True if self has a lower score than other, False otherwise
        """
        return self.__score < other.__score

    @staticmethod
    def bubble_sort(players):
        """
        Sort players by score
        @param players: list of players
        @return: sorted list of players
        """
        for i in range(len(players)):
            for j in range(len(players) - 1):
                if players[j].score < players[j + 1].score:
                    players[j], players[j + 1] = players[j + 1], players[j]

        # for i in range(len(players)):
        #     print(players[i])


# if __name__ == "__main__":
#     player = Player("1", "Andres")
#     player.add_password("password")
#     print('password ', player.verify_password("password"))
#     print('password ', player.verify_password("wrong_password"))
#     print(player)
#     print(player.id)
#     print(player.name)

#     # sort players
#     players = [Player("1", "Andres"), Player("2", "John"), Player("3", "Jane")]
#     players[0].score = 10
#     players[1].score = 5
#     players[2].score = 15
#     print('Player sort')
#     print(Player.sort(players))
