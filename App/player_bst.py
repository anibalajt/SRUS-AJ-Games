# PlayerBST class
#
# Filename: player_bst.py
# Project: SRUS-HS-Games
# Author: Andres Jarava <200700718@tafe.wa.edu.au>
# Date Created: 03/04/22
# ----------------------------------------------------------------------

from player_bnode import PlayerBNode
from player import Player


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

    @root.setter
    def root(self, root):
        """
        Setter for root
        @param root: root node
        """
        self.__root = root

    def insert(self, player):
        """
        Insert player into the BST
        @param player: player object
        """
        # Create new node
        node = PlayerBNode(player)
        if self.__root is None:  # If list is empty
            # Set root to new node
            self.root = node
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

    def search(self, name):
        """
        Search for player in BST
        @param name: name of player
        @return: player object
        """
        # Implement the following algorithm (recursively):
        # 1. If the root is None or the root node’s key matches the searched name, return it.
        # 2. If the key is less than the root’s key, search the left subtree.
        # 3. If the key is greater than the root’s key, search the right subtree

        # If root is None
        if self.__root is None:
            # Return None
            return None
        # If root's name matches name
        elif self.__root.player.name == name:
            # Return root
            return self.__root.player
        # If name is less than root's name
        elif name < self.__root.player.name:
            # Call recursive function
            return self.__search(self.__root.left, name)
        # If name is greater than root's name
        else:
            # Call recursive function
            return self.__search(self.__root.right, name)

    def __search(self, node, name):
        print("__search")
        """
        Recursive function to search for player in BST
        @param node: node
        @param name: name of player
        @return: player object
        """
        # If node is not None
        if node is not None:
            # If node's name matches name
            if node.player.name == name:
                # Return node
                return node.player
            # If name is less than node's name
            elif name < node.player.name:
                # Call recursive function
                return self.__search(node.left, name)
            # If name is greater than node's name
            else:
                # Call recursive function
                return self.__search(node.right, name)
        # If node is None
        else:
            # Return None
            return None

    def balance(self):
        """
        Balance BST
        """
        # Create new BST
        new_bst = PlayerBST()
        # Call recursive function
        self.__balance(new_bst, self.__root)
        # Set root to new BST's root
        self.root = new_bst.root

    def __balance(self, new_bst, node):
        """
        Recursive function to balance BST
        @param new_bst: new BST
        @param node: node
        """
        # If node is not None
        if node is not None:
            # Call recursive function
            self.__balance(new_bst, node.left)
            # Call recursive function
            self.__balance(new_bst, node.right)
            # Insert node into new BST
            new_bst.insert(node.player)

    def __str__(self):
        """
        String representation of BST
        @return: string representation of BST
        """
        # Create empty string
        string = ""
        # If root is not None
        if self.__root is not None:
            # Call recursive function
            string = self.__str__(self.__root)
        # Return string
        return string

    def __str__(self, node):
        """
        Recursive function to string representation of BST
        @param node: node
        @return: string representation of BST
        """
        # If node is not None
        if node is not None:
            # Return string representation of node
            return str(node.player) + "\n" + self.__str__(node.left) + self.__str__(node.right)


# test all methods on this class
# if __name__ == '__main__':
#     # create a new player BST
#     bst = PlayerBST()
#     # create a new player
#     players = [Player("1", "John"), Player("2", "Bob"), Player("3", "Tom"), Player(
#         "4", "Alan"), Player("5", "Ellen"), Player("6", "Karen"), Player("7", "Wendy")]

#     # add players to the BST
#     for player in players:
#         bst.insert(player)
