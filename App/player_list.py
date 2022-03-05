# Player list
#
# Filename: player_list.py
# Project: SRUS-HS-Games
# Author: Andres Jarava <200700718@tafe.wa.edu.au>
# Date Created: 16/2/22
# ----------------------------------------------------------------------

from .player_node import PlayerNode
# from player import Player


class DoubleLinkedList:
    """
    Double linked list class
    """

    def __init__(self):
        """
        Constructor
        @param head: head node
        @param tail: tail node
        @param size: size of list
        """
        self.__head = None
        self.__tail = None
        self.__size = 0

    @property
    def size(self):
        """
        Getter for size
        @return: size of list
        """
        return self.__size

    def insert_head(self, player):
        """
        Insert player at the start of the list
        @param player: player object
        """
        # Create new node
        node = PlayerNode(player)
        if self.__head is None:  # If list is empty
            # Set head and tail to new node
            self.__head = node
            self.__tail = node
        else:  # If list is not empty
            # Set new node's next to head
            node.next = self.__head
            # Set head's prev to new node
            self.__head.prev = node
            # Set head to new node
            self.__head = node
        # Increase size
        self.__size += 1

    def insert_tail(self, player):
        """
        Insert player at the end of the list
        @param player: player object
        """
        # Create new node
        node = PlayerNode(player)
        if self.__head is None:  # If list is empty
            # Set head and tail to new node
            self.__head = node
            self.__tail = node
        else:  # If list is not empty
            # Set new node's prev to tail
            node.prev = self.__tail
            # Set tail's next to new node
            self.__tail.next = node
            # Set tail to new node
            self.__tail = node
        # Increase size
        self.__size += 1

    def delete_head(self):
        """
        Delete head node
        """
        if self.__head is None:
            return
        else:
            # Set head to next node
            self.__head = self.__head.next
            # Set head's prev to None
            self.__head.prev = None
            # Decrease size
            self.__size -= 1

    def delete_tail(self):
        """
        Delete tail node
        """
        if self.__tail is None:
            return
        else:
            # Set tail to prev node
            self.__tail = self.__tail.prev
            # Set tail's next to None
            self.__tail.next = None
            # Decrease size
            self.__size -= 1

    def delete_by_Key(self, key):
        """
        Delete node with specified key
        @param key: key of node to delete
        """
        if self.__head is None:
            return
        else:
            node = self.__head
            while node is not None:
                if node.player.key == key:
                    if node.prev is None:
                        self.delete_head()
                    elif node.next is None:
                        self.delete_tail()
                    else:
                        node.prev.next = node.next
                        node.next.prev = node.prev
                        self.__size -= 1
                    return
                node = node.next

    def display(self, forward=True):
        """
        Iterate over list
        @param forward: direction to iterate
        """
        if forward:
            node = self.__head
            while node is not None:
                print(node.player)
                node = node.next
        else:
            node = self.__tail
            while node is not None:
                print(node.player)
                node = node.prev

    def __str__(self):
        """
        String representation of list
        @return: string
        """
        if self.__head is None:
            return "Empty list"
        else:
            node = self.__head
            string = ""
            while node is not None:
                string += str(node.player) + "\n"
                node = node.next
            return string


# if __name__ == "__main__":
    # Create list
    # list = DoubleLinkedList()
    # Insert players
    # list.insert_head(PlayerNode(Player("1", "Andres")))
    # list.insert_head(PlayerNode(Player("2", "Bobby")))
    # list.insert_head(PlayerNode(Player("3", "Cindy")))
    # list.insert_head(PlayerNode(Player("4", "Denny")))
    # list.insert_tail(PlayerNode(Player("5", "Eddy")))
    # list.insert_tail(PlayerNode(Player("6", "Fanny")))
    # list.insert_tail(PlayerNode(Player("7", "Gerry")))
    # list.insert_tail(PlayerNode(Player("8", "Harry")))
    # list.display(True)
#     # Print list
#     print(list)
#     # Delete head node
#     print(list.delete_head())
#     # Delete tail node
#     print(list.delete_tail())
#     # Print list
#     print(list)
#     # Delete head node
#     print(list.delete_head())
#     # Delete tail node
#     print(list.delete_tail())
#     # Print list
#     print(list)
#     # Delete head node
#     print(list.delete_head())
