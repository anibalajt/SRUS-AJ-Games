# PlayerBNode class
#
# Filename: player_bnode.py
# Project: SRUS-HS-Games
# Author: Andres Jarava <200700718@tafe.wa.edu.au>
# Date Created: 03/04/22
# ----------------------------------------------------------------------

class PlayerBNode:
    """
    Binary Search Tree class
    """

    def __init__(self, player):
        """
        Constructor
        @param player: player object
        """
        self.__player = player
        self.__left = None
        self.__right = None

    @property
    def player(self):
        """
        Getter for player
        @return: player object
        """
        return self.__player

    @property
    def left(self):
        """
        Getter for left
        @return: left node
        """
        return self.__left

    @left.setter
    def left(self, left):
        """
        Setter for left
        @param left: left node
        """
        self.__left = left

    @property
    def right(self):
        """
        Getter for right
        @return: right node
        """
        return self.__right

    @right.setter
    def right(self, right):
        """
        Setter for right
        @param right: right node
        """
        self.__right = right
