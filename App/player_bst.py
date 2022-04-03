# PlayerBST class
#
# Filename: player_bst.py
# Project: SRUS-HS-Games
# Author: Andres Jarava <200700718@tafe.wa.edu.au>
# Date Created: 03/04/22
# ----------------------------------------------------------------------


class PlayerBST:
    """
    Binary Search Tree class
    """

    def __init__(self):
        """
        Constructor
        @param root: root node
        """
        self.__root = None

    @property
    def root(self):
        """
        Getter for root
        @return: root node
        """
        return self.__root
