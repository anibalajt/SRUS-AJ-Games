# PlayerBST class
#
# Filename: player_bst.py
# Project: SRUS-HS-Games
# Author: Andres Jarava <200700718@tafe.wa.edu.au>
# Date Created: 03/04/22
# ----------------------------------------------------------------------

# a. Add a new file to the folder app called player_bst.py. This will contain the class that is the Binary
# Search Tree.
# b. Create a class called PlayerBST in the file you just created. Within that class, create the initialiser
# method and create an instance variable that

from player_bnode import PlayerBNode


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

    def insert(self, player):
        """
        Insert player into the BST
        @param player: player object
        """
        # Create new node
        node = PlayerBNode(player)
        if self.__root is None:  # If list is empty
            # Set root to new node
            self.__root = node
        else:  # If list is not empty
            # Set current to root
            current = self.__root
            # Set parent to None
            parent = None
            # Loop until current is None
            while current is not None:
                # Set parent to current
                parent = current
                # If player's name is less than current's name
                if player.name < current.player.name:
                    # Set current to current's left
                    current = current.left
                else:  # If player's name is greater than current's name
                    # Set current to current's right
                    current = current.right
            # If player's name is less than parent's name
            if player.name < parent.player.name:
                # Set parent's left to node
                parent.left = node
            else:  # If player's name is greater than parent's name
                # Set parent's right to node
                parent.right = node
        # Increase size
        self.__size += 1

    def search(self, name):
        """
        Search for player in BST
        @param name: name of player
        @return: player object
        """
        # If root is None or root node's key matches the searched name
        if self.__root is None or self.__root.player.name == name:
            # Return root
            return self.__root
        # If key is less than root's key
        elif name < self.__root.player.name:
            # Search left subtree
            return self.search(self.__root.left, name)
        else:
            # Search right subtree
            return self.search(self.__root.right, name)
