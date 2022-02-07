class Player:
    def __init__(self, uid, name):
        self.__uid = uid
        self.__name = name

    @property
    def uid(self):
        return self.__uid

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return (f"Player: {self.__name} with id: {self.__uid}")


t = Player(90, "John")
print(t.uid)
print(t.name)
print(t.__str__())