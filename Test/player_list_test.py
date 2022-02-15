import pytest
from app.player_list import DoubleLinkedList
from app.player import Player

class TestClass:
    def __init__(self):
        self.player_name = "John"
        self.player_uid = "John"
        self.player_object = Player(self.player_uid, self.player_name)
        self.player_uid_returned = self.player_object.uid
        self.player_name_returned = self.player_object.name
        self.player_list = DoubleLinkedList()

    def test_player_uid(self):
        assert self.player_uid_returned == self.player_uid

    def test_player_name(self):
        assert self.player_name_returned == self.player_name

    def test_player_str(self):
        assert str(
            self.player_object) == "Player: "+self.player_name+" with id: "+self.player_uid

    def test_player_list_insert_head(self):
        self.player_list.insert_head(self.player_object)
        assert self.player_list.size == 1

    def test_player_list_insert_tail(self):
        self.player_list.insert_tail(self.player_object)
        assert self.player_list.size == 1

    def test_player_list_delete_head(self):
        self.player_list.insert_head(self.player_object)
        self.player_list.delete_head()
        assert self.player_list.size == 0

    def test_player_list_delete_tail(self):
        self.player_list.insert_tail(self.player_object)
        self.player_list.delete_tail()
        assert self.player_list.size == 0

    def test_player_list_delete_head_empty(self):
        with pytest.raises(Exception):
            self.player_list.delete_head()

    def test_player_list_delete_tail_empty(self):
        with pytest.raises(Exception):
            self.player_list.delete_tail()

    def test_player_list_str_empty(self):
        assert str(self.player_list) == "Empty list"

    def test_player_list_str(self):
        self.player_list.insert_head(self.player_object)
        assert str(self.player_list) == "Player: "+self.player_name+" with id: "+self.player_uid

    def test_player_list_str_multiple(self):
        self.player_list.insert_head(self.player_object)
        self.player_list.insert_tail(self.player_object)
        assert str(self.player_list) == "Player: "+self.player_name+" with id: "+self.player_uid+"\n"+"Player: "+self.player_name+" with id: "+self.player_uid



# class TestClass:
#     def test_one(self):
#         x = "this"
#         assert "h" in x

#     def test_two(self):
#         x = "hello"
#         assert hasattr(x, "check")