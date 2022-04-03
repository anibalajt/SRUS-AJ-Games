# PlayerBST  class
#
# Filename: player_bst_test.py
# Project: SRUS-HS-Games
# Author: Andres Jarava <200700718@tafe.wa.edu.au>
# Date Created: 16/2/22
# ----------------------------------------------------------------------
import unittest
from app.player_bst import PlayerBST
from app.player import Player


class PlayerBSTTestCase(unittest.TestCase):
    """
    test case for PlayerBST class
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

    def test_insert(self):
        """
        test insert
        """
        bst = PlayerBST()
        bst.insert(self.player_object)
        bst.insert(self.player_object2)
        bst.insert(self.player_object3)
        assert bst.root.player.name == "Andres"
        assert bst.root.right.player.name == "Bobby"
        assert bst.root.right.right.player.name == "Cindy"

    def test_search(self):
        """
        test search
        """
        bst = PlayerBST()
        bst.insert(self.player_object)
        bst.insert(self.player_object2)
        bst.insert(self.player_object3)
        assert bst.search(self.player_name2).player.name == "Cindy"
        assert bst.search(self.player_name3).player.name == "Bobby"
        assert bst.search(self.player_name).player.name == "Andres"


if __name__ == '__main__':
    unittest.main()
