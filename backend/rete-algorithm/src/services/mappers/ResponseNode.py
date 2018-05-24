from src.rete.algorithm.Text import Text


class ResponseNode:
    def __init__(self):
        self.__text = Text("")
        self.__children = []

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        self.__children = value

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value
