# Player list
#
# Filename: player_list.py
# Project: SRUS-HS-Games
# Author: Andres Jarava <200700718@tafe.wa.edu.au>
# Date Created: 16/2/22
# ----------------------------------------------------------------------

from player_node import PlayerNode
from player import Player


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

    def sort(self):
        """
        Sort list
        """
        if self.__head is None:
            return
        else:
            node = self.__head
            while node is not None:
                if node.next is not None:
                    if node.player.score < node.next.player.score:
                        node.player, node.next.player = node.next.player, node.player
                node = node.next


if __name__ == "__main__":
    # Create list
    list = DoubleLinkedList()
    # Insert players
    p1 = Player("1", "Andres")
    p1.score = 10
    list.insert_head(PlayerNode(p1))

    p2 = Player("2", "Bobby")
    p2.score = 20
    list.insert_head(PlayerNode(p2))

    p3 = Player("3", "Cindy")
    p3.score = 30
    list.insert_head(PlayerNode(p3))

    p4 = Player("4", "Dennis")
    p4.score = 40
    list.insert_head(PlayerNode(p4))

    p5 = Player("5", "Eddie")
    p5.score = 50
    list.insert_head(PlayerNode(p5))

    p6 = Player("6", "Fiona")
    p6.score = 60
    list.insert_head(PlayerNode(p6))

    p7 = Player("7", "Gina")
    p7.score = 70
    list.insert_head(PlayerNode(p7))

    p8 = Player("8", "Hanna")
    p8.score = 80
    list.insert_head(PlayerNode(p8))

    p9 = Player("9", "Irene")
    p9.score = 90
    list.insert_head(PlayerNode(p9))

    p10 = Player("10", "Jack")
    p10.score = 100
    list.insert_head(PlayerNode(p10))

    # Display list
    print("\nDisplay list:")
    list.display()

    # Sort list
    print("\nSort list:")
    list.sort()
    list.display()

    # Delete node with key "1"
    print("\nDelete node with key \"1\"")
    list.delete_by_Key("1")
    list.display()

    # Delete node with key "10"
    print("\nDelete node with key \"10\"")
    list.delete_by_Key("10")
    list.display()
