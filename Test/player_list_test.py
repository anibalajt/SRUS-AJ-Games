# Player List DoubleLinkedList class
#
# Filename: player_list.py
# Project: SRUS-HS-Games
# Author: Andres Jarava <200700718@tafe.wa.edu.au>
# Date Created: 16/2/22
# ----------------------------------------------------------------------

import unittest
from app.player_list import DoubleLinkedList
from app.player import Player
from app.player_node import PlayerNode


# test case for DoubleLinkedList class
class DoubleLinkedListTestCase(unittest.TestCase):
    """
    test case for DoubleLinkedList class
    """

    def setUp(self):
        """
        set up test
        """

        self.player_name = "Andres"
        self.player_id = "1"
        self.player_object = Player(self.player_id, self.player_name)

        self.player_name2 = "Cindy"
        self.player_id2 = "2"
        self.player_object2 = Player(self.player_id2, self.player_name2)

        self.player_name3 = "Bobby"
        self.player_id3 = "3"
        self.player_object3 = Player(self.player_id3, self.player_name3)

        self.list = DoubleLinkedList()
        self.list.insert_head(PlayerNode(self.player_object))
        self.list.insert_tail(PlayerNode(self.player_object2))

    def test_size(self):
        """
        test size
        """
        assert self.list.size == 2

    def test_insert_head(self):
        """
        test insert head
        """
        self.list.insert_head(PlayerNode(self.player_object3))
        assert self.list.size == 3

    def test_insert_tail(self):
        """
        test insert tail
        """
        self.list.insert_tail(PlayerNode(self.player_object3))
        assert self.list.size == 3

    def test_delete_head(self):
        """
        test delete head
        """
        self.list.delete_head()
        assert self.list.size == 1

    def test_delete_tail(self):
        """
        test delete tail
        """
        self.list.delete_tail()
        assert self.list.size == 1

    def test_str(self):
        """
        test str
        """
        assert str(self.list) == "Player: " + self.player_name + " with id: " + self.player_id + \
            "\n" + "Player: " + self.player_name2 + " with id: " + self.player_id2 + "\n"
