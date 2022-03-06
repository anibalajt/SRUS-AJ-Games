# Player Test class
#
# Filename: player_test.py
# Project: SRUS-HS-Games
# Author: Andres Jarava <200700718@tafe.wa.edu.au>
# Date Created: 16/2/22
# ----------------------------------------------------------------------

import unittest
from app.player import Player


class PlayerTestCase(unittest.TestCase):
    """
    Test class for Player
    """

    def setUp(self):
        """
        Set up test
        """

        self.player_name = "Andres"
        self.player_id = "1"
        self.player_object = Player(self.player_id, self.player_name)
        self.player_uid_returned = self.player_object.id
        self.player_name_returned = self.player_object.name

    def test_player_uid(self):
        """
        Test player id
        """
        assert self.player_uid_returned == self.player_id

    def test_player_name(self):
        """
        Test player name
        """
        assert self.player_name_returned == self.player_name

    def test_player_add_password(self):
        """
        Test player add password
        """
        self.player_object.add_password("password")
        assert self.player_object.verify_password("password")

    def test_player_verify_password(self):
        """
        Test player verify password
        """
        self.player_object.add_password("password")
        assert self.player_object.verify_password("password")

    def test_player_verify_password_false(self):
        """
        Test player verify password false
        """
        self.player_object.add_password("password")
        assert not self.player_object.verify_password("wrong password")

    def test_player_str(self):
        """
        Test player string representation
        """
        assert str(
            self.player_object) == "Player: " + self.player_name + " with id: " + self.player_id


if __name__ == "__main__":
    unittest.main()
