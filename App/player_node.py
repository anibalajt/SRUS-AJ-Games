# Player node
#
# Filename: player_node.py
# Project: SRUS-HS-Games
# Author: Andres Jarava <200700718@tafe.wa.edu.au>
# Date Created: 16/2/22
# ----------------------------------------------------------------------

class PlayerNode:
    """
    Player node class
    """

    def __init__(self, player):
        """
        Constructor
        @param player: player object
        @param next: next node
        @param prev: previous node
        """
        self.__player = player
        self.__next = None
        self.__prev = None

    @property
    def player(self):
        """
        Getter for player
        @return: player object
        """
        return self.__player

    @property
    def next(self):
        """
        Getter for next node
        @return: next node
        """
        return self.__next

    @next.setter
    def next(self, next):
        """
        Setter for next node
        @param next: next node
        """
        self.__next = next

    @property
    def prev(self):
        """
        Getter for previous node
        @return: previous node
        """
        return self.__prev

    @prev.setter
    def prev(self, prev):
        """
        Setter for previous node
        @param prev: previous node
        """
        self.__prev = prev

    @property
    def key(self):
        """
        Getter for key
        @return: key
        """
        return self.__player.id

    def __str__(self):
        """
        String representation of node
        @return: string
        """
        return self.__player.__str__()
