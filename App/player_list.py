# create a new class that implements a
# double linked list (sometimes called a doubly linked list), so the game that uses the list can easily
# move from player to player in both directions, which is one of the requirements
# Create a method that allows you to insert a new node at the head of the list. You should consider two
# possibilities: the list is empty, or the list is not empty. For this purpose, you may consider adding a
# new method or property that tells you whether the list is empty. For example, you might call it
# is_empty and have it return a Boolean.

class DoubleLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    @property
    def size(self):
        return self.__size

    def insert_head(self, player):
        node = PlayerNode(player)
        if self.__head is None:
            self.__head = node
            self.__tail = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node
        self.__size += 1

    def insert_tail(self, player):
        node = PlayerNode(player)
        if self.__head is None:
            self.__head = node
            self.__tail = node
        else:
            node.prev = self.__tail
            self.__tail.next = node
            self.__tail = node
        self.__size += 1

    def delete_head(self):
        if self.__head is None:
            raise Exception("The list is empty")
        else:
            self.__head = self.__head.next
            self.__head.prev = None
            self.__size -= 1
            if self.__head is None:
                self.__tail = None
            return self.__head

    def delete_tail(self):
        if self.__tail is None:
            return None
        else:
            self.__tail = self.__tail.prev
            self.__tail.next = None
            self.__size -= 1
            if self.__tail is None:
                self.__head = None
            return self.__tail

    def __str__(self):
        if self.__head is None:
            return "Empty list"
        else:
            current_node = self.__head
            result = ""
            while current_node is not None:
                result += f"{current_node} -> "
                current_node = current_node.next
            return result


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


class PlayerList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = DoubleLinkedList(value)
        else:
            self.head.append(value)

    def remove(self, value):
        if self.head is not None:
            self.head.remove(value)

