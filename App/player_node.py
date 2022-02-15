# a. create a new class called PlayerNode. Add an initialiser method that takes a single
# argument called player and create 3 private instances variables. Assign the variable player to a
# private instance variable. The other two instance variables will point to the next and the previous
# node. Initialise those instance variables to None.
# b. Create the necessary getters (properties) and setters for this class. You may not need a setter for
# every instance variable.
# c. Create a property called key, which simply returns the uid property of the instance variable for the
# player object.
# d. Add a method __str__ to the PlayerNode class, which returns a string representing the node object.

class PlayerNode:
    def __init__(self, player):
        self.__player = player
        self.__next = None
        self.__prev = None

    @property
    def player(self):
        return self.__player

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, prev):
        self.__prev = prev

    @property
    def key(self):
        return self.__player.uid

    def __str__(self):
        return (f"Player: {self.__player.name} with id: {self.__player.uid}")
        