from app.player import Player
  
class Player_test:
    def __init__(self):
        self.player_name = "John"
        self.player_uid = "John"
        self.player_object = Player(self.player_uid, self.player_name)
        self.player_uid_returned = self.player_object.uid
        self.player_name_returned = self.player_object.name

    def test_player_uid(self):
        assert self.player_uid_returned == self.player_uid

    def test_player_name(self):
        assert self.player_name_returned == self.player_name

    def test_player_str(self):
        assert str(
            self.player_object) == "Player: "+self.player_name+" with id: "+self.player_uid


