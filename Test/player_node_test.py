# Player node test
#
# Filename: player_node_test.py
# Project: SRUS-HS-Games
# Author: Andres Jarava <200700718@tafe.wa.edu.au>
# Date Created: 16/2/22
# ----------------------------------------------------------------------

import unittest
from app.player_node import PlayerNode
from app.player import Player


class PlayerNodeTestCase(unittest.TestCase):
    """
    Test class for PlayerNode
    """

    def setUp(self):
        """
        Set up test
        """
        self.player_name = "Andres"
        self.player_id = "1"
        self.player_object = Player(self.player_id, self.player_name)
        self.player_node_object = PlayerNode(self.player_object)
        self.player_node_uid_returned = self.player_node_object.key
        self.player_node_player_returned = self.player_node_object.player
        self.player_node_next_returned = self.player_node_object.next
        self.player_node_prev_returned = self.player_node_object.prev

    def test_player_node_uid(self):
        """
        Test player node id
        """
        assert self.player_node_uid_returned == self.player_id

    def test_player_node_player(self):
        """
        Test player node player
        """
        assert self.player_node_player_returned == self.player_object

    def test_player_node_next(self):
        """
        Test player node next
        """
        assert self.player_node_next_returned == None

    def test_player_node_prev(self):
        """
        Test player node prev
        """
        assert self.player_node_prev_returned == None

    def test_delete_by_Key(self):
        """
        Test delete by key
        """
        self.player_node_object.delete_by_key(self.player_id)
        assert self.player_node_object.next == None
        assert self.player_node_object.prev == None
        assert self.player_node_object.player == None
        assert self.player_node_object.key == None

    def test_player_node_str(self):
        """
        Test player node string representation
        """
        assert str(
            self.player_node_object) == "Player: " + self.player_name + " with id: " + self.player_id


if __name__ == "__main__":
    unittest.main()
